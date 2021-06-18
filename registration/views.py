from django.shortcuts import render, get_object_or_404

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import *
from django.urls import reverse_lazy
from blogapp.models import *
from django.contrib.auth.views import PasswordChangeView
from registration.forms import *
class UserRegistrationForm(generic.CreateView):
    form_class = RegistrationForm
    template_name ='registration/signup.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = UserUpdateForm
    template_name ='registration/update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ResetPasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')



class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/profile.html'

    def get_context_data(self,*args, **kwargs):
        user = UserProfile.objects.all()
        page_user = get_object_or_404(UserProfile,id=self.kwargs['pk'])
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    fields = ['bio','profile_pic','website','github','instagram','twitter','facebook','linkedin','youtube']
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')


class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = ProfileCreateForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

