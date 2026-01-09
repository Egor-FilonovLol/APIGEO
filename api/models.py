from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='название')
    point = models.PointField(srid=4326,
                              geography=True,
                              verbose_name='точка')
    description = models.TextField(blank=True,
                                   verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='создано')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    message = models.TextField(verbose_name='сообщение')
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 related_name='messages')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_messages')
    created_at = models.DateTimeField(verbose_name='Создано',
                                      auto_now_add=True)
