from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from django.urls import reverse_lazy

from .models import Cliente, Fornecedor, Genero, Categoria, Filme, Locacao


class Index(TemplateView):
    template_name = "locadora/index.html"

class Sobre(TemplateView):
    template_name = "locadora/sobre.html"

class Contato(TemplateView):
    template_name = "locadora/contato.html"
    
    
    
#####  VIEWS FORNECEDOR 


class Create_Fornecedor(CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'contato', 'endereco', 'tipo_distribuicao']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo" : "Cadastro de Fornecedor",
        "botao" : "Cadastrar"
    }


class Update_Fornecedor(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'contato', 'endereco', 'tipo_distribuicao']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo" : "Edição de Fornecedor",
        "botao" : "Salvar"
    }
    
    
class Delete_Fornecedor(DeleteView):
    model = Fornecedor
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo": "Excluir Fornecedor",
        "botao": "OBLITERAR"
    }
    
    
class List_Fornecedor(ListView):
    model = Fornecedor
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Fornecedor",
        "botao": "LISTAR"
    }
    
    
class Detail_Fornecedor(DetailView):
    model = Fornecedor
    template_name = 'locadora/form.html'



# VIEWS CLIENT

class Create_Cliente(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'cpf', 'telefone', 'codigo']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Cliente",
        "botao": "Cadastrar"
    }


class Update_Cliente(UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'cpf', 'telefone', 'codigo']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Cliente",
        "botao": "Salvar"
    }


class Delete_Cliente(DeleteView):
    model = Cliente
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_cliente')
    extra_context = {
        "titulo": "Excluir Cliente",
        "botao": "OBLITERAR"
    }


class List_Cliente(ListView):
    model = Cliente
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Cliente",
        "botao": "LISTAR"
        }



class Detail_Cliente(DetailView):
    model = Cliente
    template_name = 'locadora/form.html'


# VIEWS FILME


class Create_Filme(CreateView):
    model = Filme
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Filme",
        "botao": "Cadastrar"
    }


class Update_Filme(UpdateView):
    model = Filme
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Filme",
        "botao": "Salvar"
    }


class Delete_Filme(DeleteView):
    model = Filme
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Filme",
        "botao": "OBLITERAR"
    }


class List_Filme(ListView):
    model = Filme
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Filme",
        "botao": "LISTAR"
        }
    

class Detail_Filme(DetailView):
    model = Filme
    template_name = 'locadora/form.html'



# VIEWS GENERO

class Create_Genero(CreateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Gênero",
        "botao": "Cadastrar"
    }


class Update_Genero(UpdateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Gênero",
        "botao": "Salvar"
    }


class Delete_Genero(DeleteView):
    model = Genero
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Genero",
        "botao": "OBLITERAR"
    }


class List_Genero(ListView):
    model = Genero
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Gênero",
        "botao": "LISTAR"
    }
    

class Detail_Genero(DetailView):
    model = Genero
    template_name = 'locadora/form.html'

    
# VIEWS CATEGORIA

class Create_Categoria(CreateView):
    model = Categoria
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Categoria",
        "botao": "Cadastrar"
    }


class Update_Genero(UpdateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Categoria",
        "botao": "Salvar"
    }


class Delete_Categoria(DeleteView):
    model = Categoria
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Categoria",
        "botao": "OBLITERAR"
    }


class List_Categoria(ListView):
    model = Categoria
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Categoria",
        "botao": "LISTAR"
    }
    

class Detail_Categoria(DetailView):
    model = Categoria
    template_name = 'locadora/form.html'

# VIEWS LOCACAO

class Create_Locacao(CreateView):
    model = Locacao
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Locação",
        "botao": "Cadastrar"
    }


class Update_Locacao(UpdateView):
    model = Locacao
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Locação",
        "botao": "Salvar"
    }


class Delete_Locacao(DeleteView):
    model = Locacao
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Locação",
        "botao": "OBLITERAR"
    }


class List_Locacao(ListView):
    model = Locacao
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Locação",
        "botao": "LISTAR"
    }
    

class Detail_Genero(DetailView):
    model = Locacao
    template_name = 'locadora/form.html'