from django.urls import path
from user import views

urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('active/', views.active, name='active'),
)