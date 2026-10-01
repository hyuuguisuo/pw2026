import django_filters

from .models import Categoria, Cliente, Filme, Fornecedor, Genero, Locacao


class ClienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label='Nome contém')
    email = django_filters.CharFilter(lookup_expr='icontains', label='E-mail contém')
    cpf = django_filters.CharFilter(lookup_expr='icontains', label='CPF contém')
    telefone = django_filters.CharFilter(lookup_expr='icontains', label='Telefone contém')
    codigo = django_filters.CharFilter(lookup_expr='icontains', label='Código contém')
    cadastrado_em = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),
        label='Cadastrado entre',
    )

    class Meta:
        model = Cliente
        fields = {
            'nome': ['icontains'],
            'email': ['icontains'],
            'cpf': ['icontains'],
            'telefone': ['icontains'],
            'codigo': ['icontains'],
        }


class FornecedorFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label='Nome contém')
    cnpj = django_filters.CharFilter(lookup_expr='icontains', label='CNPJ contém')
    contato = django_filters.CharFilter(lookup_expr='icontains', label='Contato contém')
    endereco = django_filters.CharFilter(lookup_expr='icontains', label='Endereço contém')
    tipo_distribuicao = django_filters.CharFilter(lookup_expr='icontains', label='Tipo de distribuição contém')

    class Meta:
        model = Fornecedor
        fields = {
            'nome': ['icontains'],
            'cnpj': ['icontains'],
            'contato': ['icontains'],
            'endereco': ['icontains'],
            'tipo_distribuicao': ['icontains'],
        }


class GeneroFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label='Nome contém')

    class Meta:
        model = Genero
        fields = {'nome': ['icontains']}


class CategoriaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label='Nome contém')

    class Meta:
        model = Categoria
        fields = {
            'nome': ['icontains'],
            'prazo_devolucao': ['gte', 'lte'],
            'preco': ['gte', 'lte'],
        }


class FilmeFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label='Título contém')
    categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(),
        label='Categoria',
    )
    genero = django_filters.ModelChoiceFilter(
        queryset=Genero.objects.all(),
        label='Gênero',
    )
    classificacao = django_filters.ChoiceFilter(choices=Filme.CLASSIFICACAO, label='Classificação')
    cadastrado_em = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),
        label='Cadastrado entre',
    )

    class Meta:
        model = Filme
        fields = {
            'titulo': ['icontains'],
            'ano_lancamento': ['gte', 'lte'],
            'categoria': ['exact'],
            'genero': ['exact'],
            'classificacao': ['exact'],
        }


class LocacaoFilter(django_filters.FilterSet):
    cliente__nome = django_filters.CharFilter(lookup_expr='icontains', label='Cliente contém')
    filme__titulo = django_filters.CharFilter(lookup_expr='icontains', label='Filme contém')
    data_locacao = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),
        label='Data de locação entre',
    )
    data_devolucao = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}),
        label='Devolução entre',
    )
    metodo_pagamento = django_filters.ChoiceFilter(choices=Locacao.METODOS_PAGAMENTO, label='Método de pagamento')

    class Meta:
        model = Locacao
        fields = {
            'cliente__nome': ['icontains'],
            'filme__titulo': ['icontains'],
            'valor': ['gte', 'lte'],
            'metodo_pagamento': ['exact'],
        }
