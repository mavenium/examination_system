from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views

from core import forms, models


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


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'index.html'
    model = models.Course


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Course
    template_name = 'course_detail.html'
