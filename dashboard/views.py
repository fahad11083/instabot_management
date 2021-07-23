from django import template
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from automation.models import *
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.all()

class DetailView(generic.DetailView):
    model = Account
    template_name = 'dashboard/detail.html'
