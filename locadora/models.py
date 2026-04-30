from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, help_text="Digite seu nome completo")
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
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

class Filme(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título", help_text="Digite o titulo do filme")
    duração = models.CharField(max_length=10, verbose_name="Duração",help_text="Digite a duração do filme")
    descricao = models.CharField(max_length=10, verbose_name="Descrição")
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)
    classificacao = models.CharField(max_length=2,  verbose_name="Classificação")
    prazo_devolucao=models.IntegerField(max_length=4,verbose_name="Prazo de devolução", help_text="Prazo em dias")
    ano_lancamento=models.IntegerField(max_length=4, verbose_name="Ano de lançamento")




class Locacao(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.PROTECT)
    filme=models.ForeignKey(Filme, on_delete=models.PROTECT)
    data_locacao=models.DateField(auto_now_add=True)
    data_devolucao=models.DateField(auto_now_add=True)


class Multa(models.Model):
    valor = models.FloatField(verbose_name="Valor")
    dias_atraso = models.IntegerField(verbose_name="Dias de Atraso")
    paga = models.BooleanField(default=False, verbose_name="Paga")
    data_gerada = models.DateTimeField(auto_now_add=True, verbose_name="Data Gerada")
    locacao = models.OneToOneField(Locacao, on_delete=models.PROTECT, related_name='multa',verbose_name="Locação")

    #def __str__(self):
        #status = "Paga" if self.paga else "Pendente"
        #return f"Multa {self.id} - R$ {self.valor} ({status})"


class Pagamento(models.Model):
    valor_pago = models.FloatField(verbose_name="Valor Pago")
    data_pagamento = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pagamento")
    metodo_pagamento = models.CharField(max_length=50, verbose_name="Método de Pagamento")
    locacao = models.ForeignKey(Locacao, on_delete=models.PROTECT, related_name='pagamentos',verbose_name="Locação")
    comprovante_gerado = models.BooleanField(default=False, verbose_name="Comprovante Gerado")