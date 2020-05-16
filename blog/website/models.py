from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

class Teste(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    explicacao = models.TextField()

