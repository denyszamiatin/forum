from django.db import models
from django.contrib.auth.models import User


TOPIC_STATE = (
    ('C', 'Closed'),
    ('O', 'Open')
)


class Moder(models.Model):
    moder = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Модераторы'


class Topic(models.Model):
    name = models.CharField(max_length=1000, unique_for_date='date')
    date = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=1, choices=TOPIC_STATE, default='O')
    author = models.ForeignKey(User)
    moder = models.ForeignKey(Moder)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Темы'

    def get_absolute_url(self):
        return "/topics/{}".format(self.pk)


class Message(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор')
    topic = models.ForeignKey(Topic, verbose_name='Тема')
    date = models.DateField('Дата')
    text = models.TextField('Текст сообщения')
    rate = models.IntegerField('Рейтинг')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = "Сообщение"
