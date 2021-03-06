from django.db import models
from workersystem.views_constant import MALE,FAMALE
# Create your models here.

class Resume(models.Model):
    photo = models.ImageField(upload_to="photo")
    sex = models.BooleanField(default=MALE)
    work_age = models.IntegerField(default=0)
    education = models.TextField()
    experience = models.TextField()
    pic1 = models.ImageField(upload_to="conclude")
    pic2 = models.ImageField(upload_to="join")
    pic3 = models.ImageField(upload_to="KPI")

    class Meta:
        db_table = 'resume'
