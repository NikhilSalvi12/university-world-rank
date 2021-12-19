from django.urls import path
from . import views

urlpatterns=[
    path('',views.userpannel,name="Userpannel"),
    path('calculate/', views.getrank ,name="CalculateRank"),
    path('data/',views.data ,name="ReferenceData"),
]