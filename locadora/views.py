from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from django.urls import reverse_lazy

from .models import Cliente, Fornecedor, Genero, Categoria


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


