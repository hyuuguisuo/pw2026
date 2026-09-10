import json
import urllib.request
import urllib.parse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin

from .models import Cliente, Fornecedor, Genero, Categoria, Filme, Locacao
from .forms import (
    ClienteForm,
    FornecedorForm,
    FilmeForm,
    GeneroForm,
    CategoriaForm,
    LocacaoForm,
)


def buscar_capa_api(request):
    """
    Busca automaticamente posters de filmes na web (Wikipedia PT API)
    Retorna a URL do poster em alta resolução e o título correspondente.
    """
    titulo = request.GET.get('titulo', '').strip()
    if not titulo:
        return JsonResponse({'sucesso': False, 'erro': 'Título não informado.'}, status=400)

    resultados = []
    search_queries = [f"{titulo} (filme)", f"{titulo} filme", titulo]
    headers = {'User-Agent': 'LocadoraApp/1.0 (aluno@instituto.edu.br)'}

    for q in search_queries:
        try:
            url_search = f"https://pt.wikipedia.org/w/api.php?action=opensearch&search={urllib.parse.quote(q)}&limit=5&namespace=0&format=json"
            req = urllib.request.Request(url_search, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as res:
                data = json.loads(res.read().decode('utf-8'))
                titles = data[1] if len(data) > 1 else []
                for t in titles:
                    try:
                        url_summary = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(t)}"
                        req2 = urllib.request.Request(url_summary, headers=headers)
                        with urllib.request.urlopen(req2, timeout=4) as res2:
                            sdata = json.loads(res2.read().decode('utf-8'))
                            thumb = sdata.get('thumbnail', {}).get('source')
                            orig = sdata.get('originalimage', {}).get('source')
                            img = orig or thumb
                            if img and any(ext in img.lower() for ext in ['.jpg', '.png', '.webp', '.jpeg']):
                                if not any(r['capa_url'] == img for r in resultados):
                                    resultados.append({
                                        'titulo': t,
                                        'capa_url': img,
                                        'descricao': sdata.get('description', ''),
                                    })
                                    if len(resultados) >= 3:
                                        break
                    except Exception:
                        continue
            if resultados:
                break
        except Exception:
            continue

    if resultados:
        return JsonResponse({'sucesso': True, 'resultados': resultados, 'principal': resultados[0]})
    return JsonResponse({'sucesso': False, 'mensagem': 'Nenhuma capa encontrada automaticamente para este título.'})



# ==============================================================================
# VIEWS ESTÁTICAS E INSTITUCIONAIS
# ==============================================================================

class Index(TemplateView):
    template_name = "locadora/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filmes = Filme.objects.select_related('categoria', 'genero').order_by('-id')
        
        # Featured movie: busca preferencialmente um filme com capa
        featured = filmes.exclude(capa='', capa_url='').first() or filmes.first()
        
        context['featured_movie'] = featured
        context['recent_movies'] = filmes[:15]
        
        # Categorias com filmes
        todas_categorias = Categoria.objects.prefetch_related('filme_set').all()
        context['categories'] = [cat for cat in todas_categorias if cat.filme_set.exists()]
        
        # Gêneros com filmes
        todos_generos = Genero.objects.prefetch_related('filme_set').all()
        context['generos'] = [gen for gen in todos_generos if gen.filme_set.exists()]
        
        context['total_filmes'] = filmes.count()
        context['total_clientes'] = Cliente.objects.count()
        context['total_locacoes'] = Locacao.objects.count()

        # Dados estruturados para Busca Instantânea e Modal Cinematográfico de Detalhes
        context['movies_json'] = [
            {
                'id': f.id,
                'titulo': f.titulo,
                'genero': f.genero.nome,
                'genero_id': f.genero.id,
                'categoria': f.categoria.nome,
                'preco': str(f.categoria.preco),
                'prazo': f.categoria.prazo_devolucao,
                'classificacao': f.classificacao,
                'classificacao_display': f.get_classificacao_display(),
                'ano': f.ano_lancamento,
                'duracao': str(f.duração),
                'descricao': f.descricao,
                'poster': f.poster_url,
                'alugar_url': f'/cadastrar/locacao/?filme={f.id}',
                'editar_url': f'/editar/filme/{f.id}/',
            }
            for f in filmes
        ]
        return context


class Sobre(TemplateView):
    template_name = "locadora/sobre.html"


class Contato(TemplateView):
    template_name = "locadora/contato.html"


class UserPasswordChangeDone(TemplateView):
    template_name = "locadora/form.html"
    extra_context = {
        "titulo": "Senha Alterada com Sucesso",
        "botao": "Voltar",
    }


# ==============================================================================
# VIEWS FORNECEDOR
# ==============================================================================

class Create_Fornecedor(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo": "Cadastro de Fornecedor",
        "botao": "Cadastrar",
    }
    success_message = "Fornecedor cadastrado com sucesso!"
    group_required = ["Funcionário", "Administrador"]

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Fornecedor(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo": "Edição de Fornecedor",
        "botao": "Salvar",
    }
    success_message = "Fornecedor atualizado com sucesso!"
    group_required = ["Funcionário", "Administrador"]


class Delete_Fornecedor(GroupRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_fornecedor')
    extra_context = {
        "titulo": "Excluir Fornecedor",
    }
    group_required = ["Administrador"]


class List_Fornecedor(GroupRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'locadora/lists/fornecedor_list.html'
    extra_context = {
        "titulo": "Listar Fornecedor",
    }
    group_required = ["Funcionário", "Administrador"]

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Fornecedor(GroupRequiredMixin, DetailView):
    model = Fornecedor
    template_name = 'locadora/lists/fornecedor_list.html'
    group_required = ["Funcionário", "Administrador"]


# ==============================================================================
# VIEWS CLIENTE
# ==============================================================================

class Create_Cliente(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_cliente')
    extra_context = {
        "titulo": "Cadastro de Cliente",
        "botao": "Cadastrar",
    }
    success_message = "Cliente cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Cliente(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_cliente')
    extra_context = {
        "titulo": "Edição de Cliente",
        "botao": "Salvar",
    }
    success_message = "Cliente atualizado com sucesso!"


class Delete_Cliente(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_cliente')
    extra_context = {
        "titulo": "Excluir Cliente",
    }
    success_message = "Cliente excluído com sucesso!"


class List_Cliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'locadora/lists/cliente_list.html'
    extra_context = {
        "titulo": "Listar Clientes",
    }

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Cliente(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'locadora/lists/cliente_list.html'


# ==============================================================================
# VIEWS FILME
# ==============================================================================

class Create_Filme(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Cadastro de Filme",
        "botao": "Cadastrar",
    }
    success_message = "Filme cadastrado com sucesso!"
    group_required = ["Funcionário", "Administrador"]

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Filme(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Edição de Filme",
        "botao": "Salvar",
    }
    success_message = "Filme atualizado com sucesso!"
    group_required = ["Funcionário", "Administrador"]


class Delete_Filme(LoginRequiredMixin, DeleteView):
    model = Filme
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_filme')
    extra_context = {
        "titulo": "Excluir Filme",
    }


class List_Filme(LoginRequiredMixin, ListView):
    model = Filme
    template_name = 'locadora/lists/filme_list.html'
    extra_context = {
        "titulo": "Catálogo de Filmes",
    }

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Filme(LoginRequiredMixin, DetailView):
    model = Filme
    template_name = 'locadora/lists/filme_list.html'


# ==============================================================================
# VIEWS GÊNERO
# ==============================================================================

class Create_Genero(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_genero')
    extra_context = {
        "titulo": "Cadastro de Gênero",
        "botao": "Cadastrar",
    }
    success_message = "Gênero cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Genero(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_genero')
    extra_context = {
        "titulo": "Edição de Gênero",
        "botao": "Salvar",
    }
    success_message = "Gênero atualizado com sucesso!"


class Delete_Genero(LoginRequiredMixin, DeleteView):
    model = Genero
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_genero')
    extra_context = {
        "titulo": "Excluir Gênero",
    }


class List_Genero(LoginRequiredMixin, ListView):
    model = Genero
    template_name = 'locadora/lists/genero_list.html'
    extra_context = {
        "titulo": "Listar Gêneros",
    }

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Genero(LoginRequiredMixin, DetailView):
    model = Genero
    template_name = 'locadora/lists/genero_list.html'


# ==============================================================================
# VIEWS CATEGORIA
# ==============================================================================

class Create_Categoria(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_categoria')
    extra_context = {
        "titulo": "Cadastro de Categoria",
        "botao": "Cadastrar",
    }
    success_message = "Categoria cadastrada com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Categoria(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_categoria')
    extra_context = {
        "titulo": "Edição de Categoria",
        "botao": "Salvar",
    }
    success_message = "Categoria atualizada com sucesso!"


class Delete_Categoria(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_categoria')
    extra_context = {
        "titulo": "Excluir Categoria",
    }


class List_Categoria(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'locadora/lists/categoria_list.html'
    extra_context = {
        "titulo": "Listar Categorias",
    }

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Categoria(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'locadora/lists/categoria_list.html'


# ==============================================================================
# VIEWS LOCAÇÃO
# ==============================================================================

class Create_Locacao(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Locacao
    form_class = LocacaoForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_locacao')
    extra_context = {
        "titulo": "Registro de Locação",
        "botao": "Registrar Locação",
    }
    success_message = "Locação registrada com sucesso!"

    def get_initial(self):
        initial = super().get_initial()
        filme_id = self.request.GET.get('filme')
        if filme_id:
            try:
                filme = Filme.objects.get(pk=filme_id)
                initial['filme'] = filme
                initial['valor'] = filme.categoria.preco
                import datetime
                from django.utils import timezone
                dt_dev = timezone.now() + datetime.timedelta(days=filme.categoria.prazo_devolucao)
                initial['data_devolucao'] = dt_dev.strftime('%Y-%m-%dT%H:%M')
            except (Filme.DoesNotExist, ValueError):
                pass
        return initial

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class Update_Locacao(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Locacao
    form_class = LocacaoForm
    template_name = 'locadora/form.html'
    success_url = reverse_lazy('listar_locacao')
    extra_context = {
        "titulo": "Edição de Locação",
        "botao": "Salvar",
    }
    success_message = "Locação atualizada com sucesso!"


class Delete_Locacao(LoginRequiredMixin, DeleteView):
    model = Locacao
    template_name = 'locadora/confirm_delete.html'
    success_url = reverse_lazy('listar_locacao')
    extra_context = {
        "titulo": "Excluir Locação",
    }


class List_Locacao(LoginRequiredMixin, ListView):
    model = Locacao
    template_name = 'locadora/lists/locacao_list.html'
    extra_context = {
        "titulo": "Listar Locações",
    }

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class Detail_Locacao(LoginRequiredMixin, DetailView):
    model = Locacao
    template_name = 'locadora/lists/locacao_list.html'