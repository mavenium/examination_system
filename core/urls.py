from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.UserCreationView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('', views.IndexView.as_view(), name='index'),
    path('course_detail_view/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail_view'),

    path('exam_results/', views.ExamResultListView.as_view(), name='exam_results'),
    path('exam_results/detail/<int:pk>/', views.ExamResultDetailView.as_view(), name='exam_results_detail_view'),
]
