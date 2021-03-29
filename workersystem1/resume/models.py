from django.db import models
from workersystem.views_constant import MALE, FEMALE


# Create your models here.

class Resume(models.Model):
    photo = models.ImageField(upload_to="photo")
    sex = models.BooleanField(default=MALE)
    age = models.IntegerField(default=18, null=True)
    work_age = models.IntegerField(default=0)
    education = models.TextField()
    experience = models.TextField()
    position = models.CharField(max_length=128, null=True)
    KPI = models.CharField(max_length=255, null=True)
    conclude = models.CharField(max_length=255, null=True)
    join = models.CharField(max_length=255, null=True)
    conclude_pic = models.ImageField(upload_to="conclude")
    join_pic = models.ImageField(upload_to="join")
    KPI_pic = models.ImageField(upload_to="KPI")
    temp_score = models.IntegerField(default=0)

    class Meta:
        db_table = 'resume'
