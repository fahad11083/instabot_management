from django import forms
from automation.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountForm(forms.Form):
    user_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def save_form(self):
        print(self.cleaned_data['password'], self.cleaned_data['email'], self.cleaned_data['user_name'])


class LikeForm(forms.Form):
    picture_link = forms.CharField()
    amount_of_likes = forms.CharField(widget=forms.NumberInput)

    def save_form(self, user_id):
        if self.cleaned_data['picture_link'] and self.cleaned_data['amount_of_likes']:
            Order.objects.create(user_id=user_id ,like_service_purchased=True, picture_link=self.cleaned_data['picture_link'], amount_of_likes=self.cleaned_data['amount_of_likes'])
            print(self.cleaned_data['picture_link'], self.cleaned_data['amount_of_likes'])


class CommentForm(forms.Form):
    picture_link = forms.CharField()
    comment_message = forms.CharField(widget=forms.Textarea)
    number_of_users = forms.CharField(widget=forms.NumberInput)


    def save_form(self, user_id):
        if self.cleaned_data['picture_link'] and self.cleaned_data['comment_message'] and self.cleaned_data['number_of_users']:
            Order.objects.create(user_id=user_id, comment_service_purchased=True, picture_link=self.cleaned_data['picture_link'], comment_message=self.cleaned_data['comment_message'], number_of_users=self.cleaned_data['number_of_users'])
            print(self.cleaned_data['picture_link'], self.cleaned_data['comment_message'], self.cleaned_data['number_of_users'])


class FollowerForm(forms.Form):
    account_link = forms.CharField()
    number_of_followers = forms.CharField(widget=forms.NumberInput)

    def save_form(self, user_id):
        if self.cleaned_data['account_link'] and self.cleaned_data['number_of_followers']:
            Order.objects.create(user_id=user_id, follower_service_purchased=True, account_link=self.cleaned_data['account_link'], number_of_followers=self.cleaned_data['number_of_followers'])
            print(self.cleaned_data['account_link'], self.cleaned_data['number_of_followers'])


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
