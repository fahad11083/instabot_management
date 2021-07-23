from django import template
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from automation.models import *
from django.views import generic
from django.views.generic.edit import FormView
from dashboard.forms import AccountForm, LikeForm, CommentForm, FollowerForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.all()


class LikeFormView(FormView):
    template_name = 'dashboard/like.html'
    form_class = LikeForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form()
        return super().form_valid(form)


class CommentFormView(FormView):
    template_name = 'dashboard/comment.html'
    form_class = CommentForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form()
        return super().form_valid(form)


class FollowerFormView(FormView):
    template_name = 'dashboard/follower.html'
    form_class = FollowerForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Account
    template_name = 'dashboard/detail.html'


class AccountFormView(FormView):
    template_name = 'dashboard/account.html'
    form_class = AccountForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form()
        return super().form_valid(form)

