from django.http import JsonResponse
from django.shortcuts import render
from user.models import User


# Create your views here.

def getResume(request):
    name = request.GET.get('name')
    users = User.objects.filter(u_name=name)
    if users.exists():
        user = users.first()
        resume = user.resume
        data = {
            'name': user.u_name,
            'photo': resume.photo,
            'sex': resume.sex,
            'work_age': resume.work_age,
            'education': resume.education,
            'experience': resume.experience,
            'pic1': resume.pic1,
            'pic2': resume.pic2,
            'pic3': resume.pic3
        }
        return JsonResponse(data)
    return JsonResponse({'msg':'此用户无背景信息'})