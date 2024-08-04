from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# Create your models here.


class User(AbstractUser):
    N_mobile = models.CharField(max_length=12, null=True, blank=True, verbose_name='تلفن')
    A_email = models.EmailField(null=False, blank=True, verbose_name='Email', unique=True, editable=False)



    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.get_full_name()
