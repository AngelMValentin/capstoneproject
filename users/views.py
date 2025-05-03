from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import SignupForm
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
    