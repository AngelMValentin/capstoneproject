from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignupForm, UpdateProfileForm
from .models import Profile


class UserLogin(LoginView):
    template_name = "users/login.html"
    
    def get_success_url(self):
        return reverse('home')

class UserSignup(CreateView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        passw = form.cleaned_data['password']
        user.set_password(passw)
        user.save()

        Profile.objects.create(user=user)

        return super().form_valid(form)
    
class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = "users/update_profile.html"
    form_class = UpdateProfileForm
    success_url = reverse_lazy("home") # should be view profile

    def get_object(self):
        # return the logged in user's profile
        profile = Profile.objects.get(user=self.request.user)
        return profile
    
class ProfileView(DetailView):
    model = Profile
    template_name = "users/profile.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('user')