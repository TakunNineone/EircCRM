from django.shortcuts import render
from django.views import generic
from .models import Cases
# Create your views here.

class CasesList(generic.ListView):
    queryset = Cases.objects.order_by('-created_on')
    template_name = 'index.html'