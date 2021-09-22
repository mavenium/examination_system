from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('', views.IndexView.as_view(), name='index'),
    path('course_detail_view/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail_view'),
]
