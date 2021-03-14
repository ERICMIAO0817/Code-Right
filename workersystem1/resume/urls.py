from django.urls import  path,include
from resume import views

urlpatterns = [
    path('getResume/',views.getResume,name='getResume'),
]