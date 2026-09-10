from django import forms
from .models import Cliente, Fornecedor, Filme, Genero, Categoria, Locacao


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'telefone', 'codigo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do cliente'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@dominio.com'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código interno do cliente'}),
        }


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'contato', 'endereco', 'tipo_distribuicao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razão social ou nome fantasia'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}),
            'contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pessoa ou canal de contato'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'tipo_distribuicao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Distribuição física, digital'}),
        }


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = [
            'titulo',
            'ano_lancamento',
            'duração',
            'classificacao',
            'categoria',
            'genero',
            'capa_url',
            'capa',
            'descricao',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Interestelar, O Poderoso Chefão...', 'id': 'id_titulo'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2024'}),
            'duração': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 120 min'}),
            'classificacao': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'capa_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://... ou clique no botão de busca',
                'id': 'id_capa_url',
            }),
            'capa': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'id': 'id_capa_file',
            }),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve sinopse ou descrição'}),
        }


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Ação, Comédia, Suspense...'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'prazo_devolucao', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Lançamento, Catálogo, Ouro...'}),
            'prazo_devolucao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prazo em dias (ex: 3)'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
        }


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'filme', 'data_devolucao', 'valor', 'valor_pago', 'data_pagamento', 'metodo_pagamento']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'filme': forms.Select(attrs={'class': 'form-select'}),
            'data_devolucao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'valor_pago': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'data_pagamento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'metodo_pagamento': forms.Select(attrs={'class': 'form-select'}),
        }
