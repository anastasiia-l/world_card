from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views as vm
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^customers/$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^customers/(?P<pk>\d+)/$', views.CustomerDetailView.as_view(), name='customer_detail'),
    url(r'^customer_registration/$', views.CustomerRegistration.as_view()),
    url(r'^change_password/$', views.ChangePassword.as_view()),
    url(r'^login/$', vm.obtain_auth_token),
]
