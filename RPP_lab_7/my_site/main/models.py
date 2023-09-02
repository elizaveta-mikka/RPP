from django.db import models
from django.urls import reverse


class Users(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    pat_name = models.CharField(max_length=20)
    nick = models.CharField(max_length=20)
    date_reg = models.DateField()
    date_b = models.DateField()

    class Meta:
        verbose_name_plural="Пользователи"


class Topics(models.Model):
    name_t = models.CharField(max_length=50)
    date_cr = models.DateField()
    n_post = models.IntegerField()
    n_view = models.IntegerField()
    n_like = models.IntegerField()

    class Meta:
        verbose_name_plural="Темы обсуждения"


class Authors(models.Model):
    n_post = models.IntegerField()
    n_view = models.IntegerField()
    n_like = models.IntegerField()
    id_user = models.OneToOneField(Users, on_delete=models.PROTECT, primary_key=True)

    class Meta:
        verbose_name_plural="Авторы"


class Posts(models.Model):
    date_post = models.DateField()
    n_view = models.IntegerField()
    n_like = models.IntegerField()
    n_comm = models.IntegerField()
    id_author = models.ManyToManyField(Authors)
    id_topic = models.ManyToManyField(Topics)

    class Meta:
        verbose_name_plural="Посты"


class Commentaries(models.Model):
    id_post = models.ForeignKey(Posts, on_delete=models.PROTECT)
    id_user = models.ForeignKey(Users, on_delete=models.PROTECT)
    date = models.DateField()
    text = models.TextField(blank=False)
    n_like = models.IntegerField()