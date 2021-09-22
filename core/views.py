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

        print(wrong, correct, questions_result)
        self.object = self.get_object()
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        return self.render_to_response(context=context)

