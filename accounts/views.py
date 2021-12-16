from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomAuthForm


class Index(View):
    def get(self, request):
        return redirect(reverse_lazy('list_booking'))


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = reverse_lazy('list_booking')
    form_class = CustomAuthForm()
