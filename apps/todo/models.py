from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='users_todo',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        unique=True
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание",
        blank=True, null=True
    )
    is_completed = models.BooleanField(
        verbose_name="Статус",
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    image = models.ImageField(
        upload_to="todo_images/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.user} {self.title}"
    
    class Meta:
        verbose_name = "Такси"
        verbose_name_plural = "Таски"