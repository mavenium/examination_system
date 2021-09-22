from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.contrib.auth import views as auth_views

from core import forms


class LoginView(auth_views.LoginView):
    """ Login viw class """
    form_class = forms.LoginForm
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:index')
        else:
            return super(LoginView, self).get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, generic.RedirectView):
    """ Logout view class """
    url = reverse_lazy('core:login')

    def get(self, request, *args, **kwargs):
        auth_views.auth_logout(request)
        return super().get(request, *args, **kwargs)


class IndexView(LoginRequiredMixin, View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context=context)
