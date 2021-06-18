from django.urls import path
from .views import*
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('signup/',UserRegistrationForm.as_view(),name='signup'),
    path('profile_edit/',UserEditView.as_view(),name='update_profile'),
    path('password/',ResetPasswordView.as_view(template_name='registration/reset_password.html'),name='password'),
    path('profile/<int:pk>',UserProfileView.as_view(),name='show_profile'),
    path('profile_edit_page/<int:pk>',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('profile_create_page/',CreateProfilePageView.as_view(),name='create_profile'),



 
]
