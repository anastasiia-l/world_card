from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from rest_framework import status
from restapi.serializers import *
from server.medic_search import find_specialty, find_by_location
from rest_framework.viewsets import ModelViewSet
from server.geocoding import get_geometry
from datetime import datetime


def send_notification(medic, call, dateTime):
    serv = Service.objects.create(medic_id=medic, call_id=call, dateTime=dateTime,
                               service_type="Notification", cost=0.0)

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class MedicViewSet(ModelViewSet):
    queryset = Medic.objects.all()
    serializer_class = MedicSerializer


class MedicalRecordCardViewSet(ModelViewSet):
    queryset = MedicalRecordCard.objects.all()
    serializer_class = MedicalRecordCardSerializer


class InsurerViewSet(ModelViewSet):
    queryset = MedicalRecordCard.objects.all()
    serializer_class = MedicalRecordCardSerializer


class MedicalInstitutionViewSet(ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer


class MedicalInsurancePolicyViewSet(ModelViewSet):
    queryset = MedicalInstitution.objects.all()
    serializer_class = MedicalInstitutionSerializer


class CallViewSet(ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer


class CustomerRegistration(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        full_name = request.data.get('full_name', '')
        DOB = request.data.get('DOB', '')

        user = User.objects.create_user(username, username, password)
        user.save()

        token = Token.objects.create(user=user)

        group = Group.objects.get(name='Customer')
        group.user_set.add(user)

        customer = Customer.objects.create(full_name=full_name, DOB=DOB, email=user.email)

        medcard = MedicalRecordCard.objects.create(customer_id=customer)
        return Response({'detail': token.key})


class MedicRegistration(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        full_name = request.data.get('full_name', '')
        inst_id = request.data.get('inst_id')
        specialty = request.data.get('specialty', '')

        user = User.objects.create_user(username, username, password)
        user.save()

        token = Token.objects.create(user=user)

        group = Group.objects.get(name='Medic')
        group.user_set.add(user)

        inst = MedicalInstitution.objects.get(institution_id=inst_id)
        medic = Medic.objects.create(institution_id=inst, specialty=specialty, full_name=full_name, email=username)

        return Response({'detail': token.key})


class FindMedic(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        result = None
        call_id = request.data.get('call_id')

        call = Call.objects.get(call_id=call_id)

        specialty = find_specialty(call.complaint, "Терапевт", "russian")

        medics = Medic.objects.filter(specialty__icontains=specialty, status="Free")
        if medics:
            nearest_medic_id = find_by_location(call.coordinates, medics.values())
            result = Medic.objects.get(medic_id=nearest_medic_id)
            send_notification(result, call,call.dateTime)

        return Response({'medic_id': result.medic_id, 'specialty': result.specialty})


class ChangePassword(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        user = get_object_or_404(User, username=request.user)
        user.set_password(request.data.get('new_password'))
        user.save()
        return Response({'detail': 'Password has been saved.'})



class Logout(generics.CreateAPIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class MedicNotification(generics.CreateAPIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        id_m = self.request.query_params.get('pk', None)
        queryset = Service.objects.all()
        medic = Service.objects.get(id_m)
        res = queryset.filter(medic_id=medic, service_type="Notification")
        return res



class CallByMedic(generics.CreateAPIView):
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        policy_id = request.data.get('policy_id')
        call_type = "ImmediateByMedic"
        coordinates = request.data.get('coordinates')
        dateTime = request.data.get('dateTime')
        complaint = request.data.get('complaint ')
        medic_id = request.data.get('medic_id ')
        full_name = request.data.get('full_name')
        service_type = "ImmediateCall"
        policy = MedicalInsurancePolicy.objects.get(policy_id)
        medic = Medic.objects.get(medic_id)
        result = Call.objects.create(policy_id=policy,call_type=call_type,coordinates=coordinates,dateTime=dateTime,complaint=complaint)
        serv = Service.objects.create(medic_id=medic, call_id=result, full_name=full_name, dateTime=dateTime,
                                   service_type=service_type)
        return result


class CallByIOT(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        policy_id = request.data.get('policy_id')
        call_type = "ImmediateByIOT"
        coordinates = request.data.get('coordinates')
        dateTime = str(datetime.now())
        complaint = request.data.get('complaint')

        policy = MedicalInsurancePolicy.objects.get(policy_id=policy_id)
        print(policy)

        result = Call.objects.create(policy_id=policy,
                                     call_type=call_type,
                                     coordinates=coordinates,
                                     dateTime=dateTime,
                                     complaint=complaint)
        medics = Medic.objects.filter(status="Free")
        if medics:
            nearest_medic = find_by_location(coordinates,medics.values())
            medic = Medic.objects.get(medic_id=nearest_medic)
            send_notification(medic,result,dateTime)
        return Response({'detail': 'Medic(' + str(medic.medic_id) +') ' +'called'})



class GetCoordinates(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        address = request.data.get('address')
        coord = get_geometry(address)
        return Response({'address': str(coord)})










