from django.views.generic import TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from django.urls import reverse_lazy

from .models import Cliente, Fornecedor, Genero, Categoria, Filme, Locacao

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class Index(TemplateView):
    template_name = "locadora/index.html"

class Sobre(TemplateView):
    template_name = "locadora/sobre.html"

class Contato(TemplateView):
    template_name = "locadora/contato.html"
    
##### AUTENTICAÇÃO VIEWS

class UserPasswordChangeDone(TemplateView):
    template_name = "locadora/form.html"
    extra_context = {
        "titulo": "Senha Alterada com Sucesso",
        "botao": "Voltar"
    }
    reverse_lazy = reverse_lazy('página_inicial')

    
#####  VIEWS FORNECEDOR 


class Create_Fornecedor(GroupRequiredMixin, CreateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'contato', 'endereco', 'tipo_distribuicao']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo" : "Cadastro de Fornecedor",
        "botao" : "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)
        print(form.instance.cadrastado_por)
        return url
    
    add_group_required = ["Funcionário", "Administrador"]

class Update_Fornecedor(GroupRequiredMixin, UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'contato', 'endereco', 'tipo_distribuicao']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo" : "Edição de Fornecedor",
        "botao" : "Salvar"
    }
    add_group_required = ["Funcionário", "Administrador"]
    
class Delete_Fornecedor(GroupRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo": "Excluir Fornecedor",
        "botao": "OBLITERAR"
    }
    add_group_required = ["Administrador"]
    
class List_Fornecedor(GroupRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Fornecedor",
        "botao": "LISTAR"
    }
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.order_by('id')

        return queryset
    
    
class Detail_Fornecedor(GroupRequiredMixin, DetailView):
    model = Fornecedor
    template_name = 'locadora/form.html'



# VIEWS CLIENT

class Create_Cliente(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['nome', 'email', 'cpf', 'telefone', 'codigo']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Cliente",
        "botao": "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)

        return url

class Update_Cliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome', 'email', 'cpf', 'telefone', 'codigo']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Cliente",
        "botao": "Salvar"
    }


class Delete_Cliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_cliente')
    extra_context = {
        "titulo": "Excluir Cliente",
        "botao": "OBLITERAR"
    }


class List_Cliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Cliente",
        "botao": "LISTAR"
        }



class Detail_Cliente(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'locadora/form.html'


# VIEWS FILME


class Create_Filme(GroupRequiredMixin, CreateView):
    model = Filme
    fields = [
        'classificacao',
        'titulo',
        'duração',
        'descricao',
        'ano_lancamento',
        'categoria',
        'genero',
    ]
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Filme",
        "botao": "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)

        return url
    add_group_required = ["Funcionário", "Administrador"]

class Update_Filme(GroupRequiredMixin, UpdateView):
    model = Filme
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Filme",
        "botao": "Salvar"
    }
    add_group_required = ["Funcionário", "Administrador"]

class Delete_Filme(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Filme",
        "botao": "OBLITERAR"
    }
    add_group_required = ["Administrador"]

class List_Filme(LoginRequiredMixin, ListView):
    model = Filme
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Filme",
        "botao": "LISTAR"
        }
    

class Detail_Filme(LoginRequiredMixin, DetailView):
    model = Filme
    template_name = 'locadora/form.html'



# VIEWS GENERO

class Create_Genero(LoginRequiredMixin, CreateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Gênero",
        "botao": "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)

        return url


class Update_Genero(LoginRequiredMixin, UpdateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Gênero",
        "botao": "Salvar"
    }


class Delete_Genero(LoginRequiredMixin, DeleteView):
    model = Genero
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Genero",
        "botao": "OBLITERAR"
    }


class List_Genero(LoginRequiredMixin, ListView):
    model = Genero
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Gênero",
        "botao": "LISTAR"
    }
    

class Detail_Genero(LoginRequiredMixin, DetailView):
    model = Genero
    template_name = 'locadora/form.html'

    
# VIEWS CATEGORIA

class Create_Categoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Categoria",
        "botao": "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)

        return url

class Update_Genero(LoginRequiredMixin, UpdateView):
    model = Genero
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Categoria",
        "botao": "Salvar"
    }


class Delete_Categoria(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Categoria",
        "botao": "OBLITERAR"
    }


class List_Categoria(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Categoria",
        "botao": "LISTAR"
    }
    

class Detail_Categoria(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'locadora/form.html'

# VIEWS LOCACAO

class Create_Locacao(LoginRequiredMixin, CreateView):
    model = Locacao
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Cadastro de Locação",
        "botao": "Cadastrar"
    }
    def form_valid(self, form):
        form.instance.cadrastado_por = self.request.user
        url = super().form_valid(form)

        return url

class Update_Locacao(LoginRequiredMixin, UpdateView):
    model = Locacao
    fields = ['classificacao', 'titulo', 'duração', 'descricao', 'ano_lancamento', 'categoria', 'genero']
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('página_inicial')
    extra_context = {
        "titulo": "Edição de Locação",
        "botao": "Salvar"
    }


class Delete_Locacao(LoginRequiredMixin, DeleteView):
    model = Locacao
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Locação",
        "botao": "OBLITERAR"
    }


class List_Locacao(LoginRequiredMixin, ListView):
    model = Locacao
    template_name = 'locadora/form.html'
    extra_context = {
        "titulo": "Listar Locação",
        "botao": "LISTAR"
    }
    

class Detail_Genero(LoginRequiredMixin, DetailView):
    model = Locacao
    template_name = 'locadora/form.html'