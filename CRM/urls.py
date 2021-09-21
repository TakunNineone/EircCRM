from . import views
from django.urls import path

urlpatterns = [
    path('',views.CasesList.as_view(), name='home'),
    #path('', views.CasesList.as_view(), name='home'),
]
