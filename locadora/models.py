from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, help_text="Digite seu nome completo")
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    codigo = models.CharField(max_length=30, verbose_name="código")
    
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    
    # cadastrado_por = mo
    def __str__(self):
        return f"{self.nome} - {self.telefone}"

class Fornecedor(models.Model):
    nome = models.CharField(max_length = 50, help_text = "Digite seu nome completo")
    cnpj = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name="endereço")
    tipo_distribuicao = models.CharField(max_length=50, verbose_name="tipo de distribuição")

    def __str__(self):
        return f"{self.nome}"


class Genero(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    def __str__(self):
        return f"{self.titulo}\n{self.descricao}\n"

    
class Categoria(models.Model):
    # genero = models.OneToOneField()
    multa_atraso = models.FloatField()
    valor_mensal = models.FloatField()
    valor_promocao = models.FloatField()

    # def __str__(self):
    #     return f"{self.nome}"
