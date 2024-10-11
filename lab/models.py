from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField('Название', max_length=50)
    discription = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
