from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index_view, name='index'),
    path(r'signup', views.register, name='signup'),
    path('likes/', views.LikeFormView.as_view(), name='likes'),
    path('comments/', views.CommentFormView.as_view(), name='comments'),
    path('followers/', views.FollowerFormView.as_view(), name='followers'),
    path('form/', views.AccountFormView.as_view()),
]
