from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=25)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

