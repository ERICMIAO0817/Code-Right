from django.urls import path,include

from search import views

urlpatterns = [
    path('DIY_ways',views.DIY_ways,name='DIY_ways')
]