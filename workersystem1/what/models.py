from django.db import models
from workersystem.views_constant import MALE,FAMALE
# Create your models here.

class User(models.Model):
    u_username = models.CharField(max_length=64,unique=True)
    u_password = models.CharField(max_length=64)
    u_sex = models.IntegerField(default=MALE)
    u_phone = models.CharField(max_length=128)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    u_position = models.IntegerField(default=0)
    u_icon = models.ImageField(upload_to='icon/%Y/%m/%d/')
    objects = models.Manager()
    DoesNotExist = models.Manager()
    class Meta:
        db_table = 'work_user'
    


