from django import template
from django.forms.forms import Form
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from automation.models import *
from django.views import generic
from django.views.generic.edit import FormView
from dashboard.forms import AccountForm, LikeForm, CommentForm, FollowerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_view(request):
    current_user = request.user
    print('current_user', current_user.id)
    return render(request, 'dashboard/index.html')


class LikeFormView(FormView):
    template_name = 'dashboard/like.html'
    form_class = LikeForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form(self.request.user.id)
        return super().form_valid(form)

class CommentFormView(FormView):
    template_name = 'dashboard/comment.html'
    form_class = CommentForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form(self.request.user.id)
        return super().form_valid(form)


class FollowerFormView(FormView):
    template_name = 'dashboard/follower.html'
    form_class = FollowerForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save_form(self.request.user.id)
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

