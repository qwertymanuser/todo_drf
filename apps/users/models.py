from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=200,
        verbose_name="Телефонный номер",
        help_text="Например: +996 (555) 55 55 55"
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
        help_text="Например: 18",
        blank=True, null=True
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"