from django import forms

class AccountForm(forms.Form):
    user_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def save_form(self):
        print(self.cleaned_data['password'], self.cleaned_data['email'], self.cleaned_data['user_name'])


class LikeForm(forms.Form):
    picture_link = forms.CharField()
    amount_of_likes = forms.CharField(widget=forms.NumberInput)

    def save_form(self):
        print(self.cleaned_data['picture_link'], self.cleaned_data['amount_of_likes'])


class CommentForm(forms.Form):
    picture_link = forms.CharField()
    comment_message = forms.CharField(widget=forms.Textarea)
    number_of_users = forms.CharField(widget=forms.NumberInput)


    def save_form(self):
        print(self.cleaned_data['picture_link'], self.cleaned_data['comment_message'], self.cleaned_data['number_of_users'])


class FollowerForm(forms.Form):
    account_link = forms.CharField()
    number_of_followers = forms.CharField(widget=forms.NumberInput)

    def save_form(self):
        print(self.cleaned_data['account_link'], self.cleaned_data['number_of_followers'])
