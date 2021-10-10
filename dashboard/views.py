from django.shortcuts import render
from automation.models import *
from django.views import generic
from django.views.generic.edit import FormView
import dashboard
from dashboard.forms import AccountForm, LikeForm, CommentForm, FollowerForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import  render, redirect
from django.urls import reverse
import pdb

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


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard:index")

