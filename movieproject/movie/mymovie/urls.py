from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("aftersignup/",views.aftersignup),
    path("afterverify/",views.afterverify),
    path("viewall/",views.viewall)
    
]