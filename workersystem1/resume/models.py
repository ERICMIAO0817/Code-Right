from django.db import models
from workersystem.views_constant import MALE, FAMALE


# Create your models here.

class Resume(models.Model):
    photo = models.ImageField(upload_to="photo")
    sex = models.BooleanField(default=MALE)
    age = models.IntegerField(default=18, null=True)
    work_age = models.IntegerField(default=0)
    education = models.TextField()
    experience = models.TextField()
    position = models.CharField(max_length=128, null=True)
    KPI = models.IntegerField(default=0)
    conclude = models.IntegerField(default=0)
    join = models.IntegerField(default=0)
    pic1 = models.ImageField(upload_to="conclude")
    pic2 = models.ImageField(upload_to="join")
    pic3 = models.ImageField(upload_to="KPI")

    class Meta:
        db_table = 'resume'
