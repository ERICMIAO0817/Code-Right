from django.http import JsonResponse
from django.shortcuts import render
from workersystem.views_constant import KPI, conclude, join, getAlpha
from user.models import User


# Create your views here.

def getResume(request):
    name = request.GET.get('name')
    print(name)
    users = User.objects.filter(u_username=name)
    if users.exists():
        user = users.first()
        resume = user.resume
        if len(resume.KPI_pic.name) == 0:
            kpi = resume.KPI
            lis = kpi.split('#')
            KPI_list = []
            for i in lis:
                KPI_list.append(int(i))
            KPI(KPI_list, name)
            resume.KPI_pic.name = 'KPI/' + name + '_KPI.png'
            resume.save()
            print('what')
        if len(resume.conclude_pic.name) == 0:
            con = resume.conclude
            print(con)
            lis = con.split('#')
            conclude_list = []
            for i in lis:
                conclude_list.append(float(i))
            conclude(conclude_list, name)
            resume.conclude_pic.name = 'conclude/' + name + '_con.png'
            resume.save()
        if len(resume.join_pic.name) == 0:
            jo = resume.join
            lis = jo.split('#')
            join_list = []
            for i in lis:
                join_list.append(float(i))
            join(join_list, name)
            resume.join_pic.name = 'join/' + name + '_join.png'
            resume.save()
        data = {
            'name': user.u_name,
            'photo': 'http://localhost:8000/static/uploads/' + resume.photo.name,
            'sex': resume.sex,
            'age': resume.age,
            'email': resume.user.u_email,
            'work_age': resume.work_age,
            'education': resume.education,
            'experience': resume.experience,
            'pic1': 'http://localhost:8000/static/uploads/' + resume.KPI_pic.name,
            'pic2': 'http://localhost:8000/static/uploads/' + resume.join_pic.name,
            'pic3': 'http://localhost:8000/static/uploads/' + resume.conclude_pic.name
        }
        return JsonResponse(data)
    return JsonResponse({'msg': '此用户无背景信息'})


def getScore(request):
    name = request.POST.get('name')
    users = User.objects.filter(u_username=name)
    user = users.first()
    group1 = request.POST.get('group1')
    group2 = request.POST.get('group2')
    group3 = request.POST.get('group3')
    group4 = request.POST.get('group4')
    A1 = getAlpha(group1)
    A2 = getAlpha(group2)
    A3 = getAlpha(group3)
    A4 = getAlpha(group4)
    lis = str(7 - A1) + '#' + str((A2 + A3) / 2) + '#' + str(A1) + '#' + str(A4) + '#' + str(7 - A4)
    resume = user.resume
    resume.conclude = lis
    con = resume.conclude
    print(con)
    lis = con.split('#')
    conclude_list = []
    for i in lis:
        conclude_list.append(float(i))
    conclude(conclude_list, name)
    resume.conclude_pic.name = 'conclude/' + name + '_con.png'
    resume.save()
    return JsonResponse({'picture': 'http://localhost:8000/static/uploads/'+resume.conclude_pic.name})