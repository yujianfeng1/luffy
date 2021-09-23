from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telephone = models.CharField(max_length=11)
    icon = models.ImageField(upload_to='icon', default='icon/default.jfif')

    class Meta:
        db_table = 'luffy_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
