from django.http import JsonResponse
from django.shortcuts import render

from user.models import User


# Create your views here.

def getResume(request):
    name = request.GET.get('name')
    print(name)
    users = User.objects.filter(u_username=name)
    if users.exists():
        user = users.first()
        resume = user.resume
        data = {
            'name': user.u_name,
            'photo': 'http://localhost:8000/static/uploads/' + resume.photo.name,
            'sex': resume.sex,
            'age': resume.age,
            'email':resume.user.u_email,
            'work_age': resume.work_age,
            'education': resume.education,
            'experience': resume.experience,
            'pic1': 'http://localhost:8000/static/uploads/' + resume.pic1.name,
            'pic2': 'http://localhost:8000/static/uploads/' + resume.pic2.name,
            'pic3': 'http://localhost:8000/static/uploads/' + resume.pic3.name
        }
        return JsonResponse(data)
    return JsonResponse({'msg': '此用户无背景信息'})
