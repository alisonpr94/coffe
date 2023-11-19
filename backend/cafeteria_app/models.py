from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class Venda(models.Model):
    produtos = models.ManyToManyField(Produto)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

class MetaFuncionario(models.Model):
    funcionario = models.OneToOneField(User, on_delete=models.CASCADE)
    meta_vendas = models.DecimalField(max_digits=10, decimal_places=2)