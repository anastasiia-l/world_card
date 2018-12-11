from server.models import Customer
from restapi.serializers import CustomerSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from  rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from  django.views.generic import TemplateView


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRegistration(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    def post(self, request, *args, **kwargs):
        print(request.data)
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        print(username)
        print(password)
        user = User.objects.create_user(username, username, password)
        user.save()
        token = Token.objects.create(user = user)
        return Response({'detail':'User has been created with token: ' + token.key})

class ChangePassword(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        print(request.data)
        user = get_object_or_404(User, username= request.user)
        user.set_password(request.data.get('new_password'))
        user.save()
        return Response({'detail': 'Password has been saved.'})