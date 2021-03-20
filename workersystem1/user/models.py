from django.db import models
from resume.models import Resume
from workersystem.views_constant import MALE, FEMALE


# Create your models here.

class Company(models.Model):
    c_id = models.IntegerField(default=0, primary_key=True)
    c_name = models.CharField(max_length=128, unique=True)
    c_agent = models.CharField(max_length=64)
    c_logo = models.ImageField(upload_to='logo/%Y')
    c_email = models.CharField(max_length=128)
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        db_table = 'company'


class User(models.Model):
    u_username = models.CharField(max_length=64, unique=True)
    u_password = models.CharField(max_length=254)
    u_name = models.CharField(max_length=128)
    u_idcard = models.CharField(max_length=128)
    u_email = models.CharField(max_length=128, unique=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    resume = models.OneToOneField(Resume,null=True,on_delete=models.CASCADE)
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        db_table = 'work_user'
