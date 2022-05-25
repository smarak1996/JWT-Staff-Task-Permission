from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('users/', views.UserView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('user/', views.UserTypeApiView.as_view(), name='user'),
    path('task/', views.TaskListApiView.as_view(), name='task'),
    path('task/<int:pk>/', views.TaskDetailApiView.as_view(), name='task_detail'),


]
