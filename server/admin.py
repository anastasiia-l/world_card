from django.contrib import admin
from .models import Call,Customer,MedicalInstitution,Medic,MedicalInsurancePolicy,MedicalRecordCard, Authorization, Insurer,Service

admin.site.register(Call)
admin.site.register(Customer)
admin.site.register(MedicalRecordCard)
admin.site.register(Medic)
admin.site.register(MedicalInsurancePolicy)
admin.site.register(MedicalInstitution)
admin.site.register(Insurer)
admin.site.register(Service)
admin.site.register(Authorization)
