from rest_framework import serializers
from server.models import Customer, MedicalRecordCard, Insurer, \
    MedicalInstitution, Service, Call, MedicalInsurancePolicy, Medic


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'full_name', 'DOB', 'nationality',
                  'international_passport', 'email')

class MedicalRecordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecordCard
        fields = ('customer_id', 'contraindications', 'allergies',
                  'past_illnesses')

class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = ('insurer_id', 'name', 'contacts', 'coordinates', 'email')

class MedicalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInstitution
        fields = ('institution_id', 'coordinates', 'email')

class MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = ('medic_id', 'institution_id', 'specialty', 'full_name',
                  'status', 'coordinates', 'email')

class MedicalInsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInsurancePolicy
        fields = ('policy_id', 'customer_id', 'insurer_id', 'policy_type',
                  'limit', 'duration', 'region')

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('call_id', 'policy_id', 'call_type', 'coordinates',
                  'dateTime', 'complaint')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_id', 'medic_id', 'call_id', 'service_type',
                  'full_name', 'dateTime', 'cost', 'status')

