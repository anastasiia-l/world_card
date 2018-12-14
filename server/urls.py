from rest_framework.authtoken import views as vm
from django.conf.urls import url
from . import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^calls/$', views.CallViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^calls/(?P<pk>\d+)/$', views.CallViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^services/$', views.ServiceViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^services/(?P<pk>\d+)/$', views.ServiceViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^institutions/$', views.MedicalInstitutionViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^institutions/(?P<pk>\d+)/$', views.MedicalInstitutionViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^policies/$', views.MedicalInsurancePolicyViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^policies/(?P<pk>\d+)/$', views.MedicalInsurancePolicyViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    )),
    url(r'^recordcards/$', views.MedicalRecordCardViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^recordcards/(?P<pk>\d+)/$', views.MedicalRecordCardViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^insurers/$', views.InsurerViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^insurers/(?P<pk>\d+)/$', views.InsurerViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^medics/$', views.MedicViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^medics/(?P<pk>\d+)/$', views.MedicViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    url(r'^customers/$', views.CustomerViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    url(r'^customers/(?P<pk>\d+)/$', views.CustomerViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),


    url(r'^medics/find/$', views.FindMedic.as_view()),
    url(r'^medics/notification/(?P<pk>\d+)/$', views.MedicNotification.as_view()),
    url(r'^medics/createcall/$', views.CallByMedic.as_view()),

    url(r'^iot/createcall/$', views.CallByIOT.as_view()),

    url(r'^coordinates/$', views.GetCoordinates.as_view()),

    url(r'^customers/registration/$', views.CustomerRegistration.as_view()),
    url(r'^medics/registration/$', views.MedicRegistration.as_view()),

    url(r'^change_password/$', views.ChangePassword.as_view()),
    url(r'^login/$', vm.obtain_auth_token),
    url(r'^logout/$', views.Logout.as_view()),
]
