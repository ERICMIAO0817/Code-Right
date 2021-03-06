from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from login.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        user = User()
        user.u_username = request.POST.get('username')
        user.u_password = request.POST.get('password')
        user.u_sex = request.POST.get('sex')
        user.u_phone = request.POST.get('phone')
        user.save()
