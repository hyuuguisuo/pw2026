from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, help_text="Digite seu nome completo")
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    codigo = models.CharField(max_length=30, verbose_name="código")
    
    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.telefone}"

class Fornecedor(models.Model):
    nome = models.CharField(max_length = 50, help_text = "Digite seu nome completo")
    cnpj = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, verbose_name="endereço")
    tipo_distribuicao = models.CharField(max_length=50, verbose_name="tipo de distribuição")

    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        ordering = ['-id']  # Sempre trará os mais novos primeiro por padrão

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)

    
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome")
    prazo_devolucao=models.IntegerField(verbose_name="Prazo de devolução", help_text="Prazo em dias", default=30)
    preco = models.DecimalField(verbose_name="preço", decimal_places=2, max_digits=6)

    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"

class Filme(models.Model):
    CLASSIFICACAO = (
        ("L", "Livre"),
        ("A10", "10 anos"),
        ("A12", "12 anos"),
        ("A14" , "14 anos"),
        ("A16" , "16 anos"),
        ("A18", "18 anos")
    )
    titulo = models.CharField(max_length=50, verbose_name="Título", help_text="Digite o titulo do filme")
    duração = models.CharField(max_length=10, verbose_name="Duração",help_text="Digite a duração do filme")
    descricao = models.CharField(max_length=255, blank=True, verbose_name="Descrição")
    ano_lancamento=models.IntegerField(verbose_name="Ano de lançamento")
    
    classificacao = models.CharField(verbose_name="Classificação", choices=CLASSIFICACAO)
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)
    genero=models.ForeignKey(Genero, on_delete=models.PROTECT)

    capa = models.ImageField(upload_to='capas/', null=True, blank=True, verbose_name="Capa (Upload de Arquivo)")
    capa_url = models.URLField(max_length=500, null=True, blank=True, verbose_name="Capa (Link da Web)")

    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento})"

    @property
    def poster_url(self):
        if self.capa:
            try:

               # O getattr evita o falso positivo do Pylint e lê a URL do arquivo upado
               # • self.capa.url: É gerado automaticamente pelo Django quando o usuário faz o upload de um arquivo de imagem do computador dele.
               #• self.capa_url: Geralmente é um link de texto puro que você cola manualmente(por exemplo, um link da internet).

                return getattr(self.capa, 'url', None)
            except Exception:
                pass
        if self.capa_url:
            return self.capa_url
        return None

class Locacao(models.Model):
    METODOS_PAGAMENTO = (
        ("PIX", "PIX"),
        ("CC", "Cartão de crédito"),
        ("débito", "Débito"),
        ("boleto" , " Boletos Bancários"),
        ("carteira digital", "e-wallets"),
        
    )
    cliente=models.ForeignKey(Cliente, on_delete=models.PROTECT)
    filme=models.ForeignKey(Filme, on_delete=models.PROTECT)
    
    data_locacao=models.DateTimeField(auto_now_add=True)
    data_devolucao=models.DateTimeField()

    valor = models.DecimalField(verbose_name="preço", decimal_places=2, max_digits=6)
    valor_pago = models.DecimalField(verbose_name="preço", decimal_places=2, max_digits=6, default=0)
    data_pagamento = models.DateTimeField(verbose_name="Data do Pagamento", null=True, blank=True)
    metodo_pagamento = models.CharField(max_length=50, verbose_name="Método de Pagamento", blank=True, null=True, choices=METODOS_PAGAMENTO)

    cadastrado_por = models.ForeignKey("auth.User", on_delete=models.PROTECT, null=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #O self.id não funcionava, pois o framework web do Django não cria o id do objeto até que ele seja salvo
        #Como estamos na classe, não tem objetos sendo criados e consequentemente não existem atributos de id, então a instância "id" não existe
        return f"Locação #{self.pk} - {self.filme.titulo} ({self.cliente.nome})"

    def save(self):
        # User biblioteca relativedelta
        if not self.data_devolucao:
            #                        data           +       int em dias
            self.data_devolucao = self.data_locacao + self.filme.categoria.prazo_devolucao

        if not self.valor:
            # pega também o valor
            self.valor = self.filme.categoria.preco

        super().save()
