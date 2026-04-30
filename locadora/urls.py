from django.urls import path
from .views import *

urlpatterns = [
  path("inicio/", Index.as_view(), name="página_inicial"),
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
    
    
    

  ]