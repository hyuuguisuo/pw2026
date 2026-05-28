from django.urls import path
from .views import *

from django.contrib.auth.views import (
     LoginView,
     LogoutView,
     PasswordChangeView,
)

urlpatterns = [

  # URL DE AUTENTICAÇÃO
  
  path("login/", LoginView.as_view(
      template_name ='locadora/form.html',
      extra_context = {
          "titulo": "Login",
          "botao": "Entrar"
      }
  ), name="login"),
  path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
  path("alterar_senha/", PasswordChangeView.as_view(
     template_name = 'locadora/form.html',
     extra_context = {
         "titulo": "Alterar Senha",
         "botao": "Salvar"
     }    
  ), name="alterar_senha"),


  path("", Index.as_view(), name="página_inicial"),
  path("sobre/", Sobre.as_view(), name="sobre"),
  path("contato/", Contato.as_view(), name="contato"),
  
  # ## URL FORNECEDOR
  path("cadastrar/fornecedor/", Create_Fornecedor.as_view(), name="novo_fornecedor"),
  path("listar/fornecedor/", List_Fornecedor.as_view(), name="listar_fornecedor"),
  path("excluir/fornecedor/<int:pk>/", Delete_Fornecedor.as_view(), name="excluir_fornecedor"),
  path("editar/fornecedor/<int:pk>/", Update_Fornecedor.as_view(), name="editar_fornecedor"),
  path("detalhes/fornecedor/<int:pk>/", Detail_Fornecedor.as_view(), name="detalhes_fornecedor"),
  
  #URL CLIENTES
  
  path("cadastrar/cliente/", Create_Cliente.as_view(), name="novo_cliente"),
  path("listar/cliente/", List_Cliente.as_view(), name="listar_cliente"),
  path('excluir/cliente/<int:pk>/', Delete_Cliente.as_view(), name="excluir_cliente"),
  path("editar/cliente/<int:pk>/", Update_Cliente.as_view(), name="editar_cliente"),
  path("detalhes/cliente/<int:pk>/", Detail_Cliente.as_view(), name="detalhes_cliente"),
  
  # URL FILMES

  path("cadastrar/filme/", Create_Filme.as_view(), name="novo_filme"),
  path("listar/filme/", List_Filme.as_view(), name="listar_filme"),
  path('excluir/filme/<int:pk>/', Delete_Filme.as_view(),
       name="excluir_filme"),
  path("editar/filme/<int:pk>/", Update_Filme.as_view(),
       name="editar_filme"),
  path("detalhes/filme/<int:pk>/", Detail_Filme.as_view(), name="detalhes_filme"),
  
  # URL GENERO

  path("cadastrar/genero/", Create_Genero.as_view(), name="novo_Genero"),
  path("listar/genero/", List_Genero.as_view(), name="listar_Genero"),
  path('excluir/genero/<int:pk>/', Delete_Genero.as_view(),
       name="excluir_genero"),
  path("editar/genero/<int:pk>/", Update_Genero.as_view(),
       name="editar_genero"),
  path("detalhes/genero/<int:pk>/", Detail_Genero.as_view(), name="detalhes_Genero"),
  
  
  # URL CATEGORIA

  path("cadastrar/categoria/", Create_Filme.as_view(), name="novo_filme"),
  path("listar/filme/", List_Filme.as_view(), name="listar_filme"),
  path('excluir/filme/<int:pk>/', Delete_Filme.as_view(),
       name="excluir_filme"),
  path("editar/filme/<int:pk>/", Update_Filme.as_view(),
       name="editar_filme"),

]