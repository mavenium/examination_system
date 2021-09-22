from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

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


class UserCreationView(generic.CreateView):
    """ User Creation viw class """
    form_class = UserCreationForm
    success_url = reverse_lazy('core:login')
    template_name = 'auth/signup.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('core:index')
        else:
            return super(UserCreationView, self).get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, generic.RedirectView):
    """ Logout view class """
    url = reverse_lazy('core:login')

    def get(self, request, *args, **kwargs):
        auth_views.auth_logout(request)
        return super().get(request, *args, **kwargs)


class IndexView(LoginRequiredMixin, generic.ListView):
    """ Index viw class to show courses """
    template_name = 'index.html'
    model = models.Course


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    """ Course detail viw class to show course detail and collect user answers """
    model = models.Course
    template_name = 'course_detail.html'

    def post(self, request, *args, **kwargs):
        wrong = 0
        correct = 0

        course = models.Course.objects.get(pk=self.kwargs['pk'])
        questions_result = []
        for question in course.exam.questions.all():
            answer_is_correct = False
            user_answer = int(request.POST.get(f'{question.pk}'))
            if question.correct_answer == user_answer:
                answer_is_correct = True
                correct += 1
            else:
                wrong += 1

            questions_result.append({
                'question': question.title,
                'question_id': question.id,
                'user_answer': models.Choice.objects.get(pk=user_answer).__str__(),
                'correct_answer': models.Choice.objects.get(pk=question.correct_answer).__str__(),
                'answer_is_correct': answer_is_correct
            })

        exam_result = models.ExamResult.objects.create(
            user=self.request.user,
            course_id=self.kwargs['pk'],
            exam_id=course.exam.id,
            result=questions_result,
            wrong_count=wrong,
            correct_count=correct
        )

        return HttpResponseRedirect(reverse('core:exam_results_detail_view', args=[exam_result.pk]))


class ExamResultListView(LoginRequiredMixin, generic.ListView):
    """ Exam result viw class to show exam results """
    template_name = 'exam_result_list.html'
    model = models.ExamResult

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).defer('result')


class ExamResultDetailView(LoginRequiredMixin, generic.DetailView):
    """ Course detail detail viw class to show exam result detail """
    model = models.ExamResult
    template_name = 'exam_result_detail.html'
