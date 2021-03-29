import random

from django.http import JsonResponse
from django.shortcuts import render
from resume.models import Resume
from user.models import User


# Create your views here.
def DIY_ways(requests):
    join = requests.POST.get('n1')
    experience = requests.POST.get('n2')
    KPI = requests.POST.get('n3')
    attendance = requests.POST.get('n4')
    project = requests.POST.get('n5')
    users = User.objects.all()
    for user in users:
        resume = user.resume
        score1 = 90*float(join)
        score2 = 0
        if resume.work_age>10:
            score2 = 90*float(experience)
        else:
            score2 = 80*float(experience)
        kpi = resume.KPI[0:2]
        print(kpi)
        score3 = int(kpi)*float(KPI)
        score4 = random.randrange(80,90)*float(attendance)
        score5 = int(resume.join[0:2])*float(project)
        resume.temp_score = score1+score2+score3+score4+score5
        resume.save()
    resumes = Resume.objects.order_by('-temp_score')
    name_lis = []
    for i in resumes:
        name_lis.append(i.user.u_name)
    print(name_lis)
    return JsonResponse({'result':name_lis})

