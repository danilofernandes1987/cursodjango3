from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

    full_name.admin_order_field = 'title'

class Teste(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    explicacao = models.TextField()

class Agenda(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.FloatField()
    categoria = models.ForeignKey("Categoriasagenda", on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Categoriasagenda(models.Model):
    nomecategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nomecategoria