from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import (
    Index,
    Sobre,
    Contato,
    UserPasswordChangeDone,
    # Fornecedor
    Create_Fornecedor,
    List_Fornecedor,
    Update_Fornecedor,
    Delete_Fornecedor,
    Detail_Fornecedor,
    # Cliente
    Create_Cliente,
    List_Cliente,
    Update_Cliente,
    Delete_Cliente,
    Detail_Cliente,
    # Filme
    Create_Filme,
    List_Filme,
    Update_Filme,
    Delete_Filme,
    Detail_Filme,
    # Genero
    Create_Genero,
    List_Genero,
    Update_Genero,
    Delete_Genero,
    Detail_Genero,
    # Categoria
    Create_Categoria,
    List_Categoria,
    Update_Categoria,
    Delete_Categoria,
    Detail_Categoria,
    # Locacao
    Create_Locacao,
    List_Locacao,
    Update_Locacao,
    Delete_Locacao,
    Detail_Locacao,
    # API
    buscar_capa_api,
    UsernameRecoveryView,
)

urlpatterns = [
    # ==========================================================================
    # API AUXILIAR
    # ==========================================================================
    path("api/buscar-capa/", buscar_capa_api, name="api_buscar_capa"),
    # ==========================================================================
    # AUTENTICAÇÃO
    # ==========================================================================
    path("login/", LoginView.as_view(
        template_name='locadora/form.html',
        extra_context={
            "titulo": "Acessar Sistema",
            "botao": "Entrar"
        }
    ), name="login"),
    path("recuperar-usuario/", UsernameRecoveryView.as_view(), name="recuperar_usuario"),
    path("recuperar-senha/", PasswordResetView.as_view(
        template_name="locadora/form.html",
        email_template_name="locadora/password_reset_email.html",
        subject_template_name="locadora/password_reset_subject.txt",
        success_url=reverse_lazy("senha_recuperacao_enviada"),
        extra_context={
            "titulo": "Recuperar Senha",
            "botao": "Enviar instruções",
        },
    ), name="senha_recuperacao"),
    path("recuperar-senha/enviado/", PasswordResetDoneView.as_view(
        template_name="locadora/password_reset_done.html",
    ), name="senha_recuperacao_enviada"),
    path("recuperar-senha/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        template_name="locadora/password_reset_confirm.html",
        success_url=reverse_lazy("senha_recuperacao_concluida"),
    ), name="senha_reset_confirm"),
    path("recuperar-senha/concluido/", PasswordResetCompleteView.as_view(
        template_name="locadora/password_reset_complete.html",
    ), name="senha_recuperacao_concluida"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("alterar_senha/", PasswordChangeView.as_view(
        template_name='locadora/form.html',
        extra_context={
            "titulo": "Alterar Senha",
            "botao": "Atualizar Senha"
        }
    ), name="alterar_senha"),
    path("senha/alterar/concluido/", UserPasswordChangeDone.as_view(), name="senha_alterada_concluida"),

    # ==========================================================================
    # PÁGINAS GERAIS / INSTITUCIONAIS
    # ==========================================================================
    path("", Index.as_view(), name="página_inicial"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    path("contato/", Contato.as_view(), name="contato"),

    # ==========================================================================
    # FILMES
    # ==========================================================================
    path("cadastrar/filme/", Create_Filme.as_view(), name="novo_filme"),
    path("listar/filme/", List_Filme.as_view(), name="listar_filme"),
    path("editar/filme/<int:pk>/", Update_Filme.as_view(), name="editar_filme"),
    path("excluir/filme/<int:pk>/", Delete_Filme.as_view(), name="excluir_filme"),
    path("detalhes/filme/<int:pk>/", Detail_Filme.as_view(), name="detalhes_filme"),

    # ==========================================================================
    # CLIENTES
    # ==========================================================================
    path("cadastrar/cliente/", Create_Cliente.as_view(), name="novo_cliente"),
    path("listar/cliente/", List_Cliente.as_view(), name="listar_cliente"),
    path("editar/cliente/<int:pk>/", Update_Cliente.as_view(), name="editar_cliente"),
    path("excluir/cliente/<int:pk>/", Delete_Cliente.as_view(), name="excluir_cliente"),
    path("detalhes/cliente/<int:pk>/", Detail_Cliente.as_view(), name="detalhes_cliente"),

    # ==========================================================================
    # FORNECEDORES
    # ==========================================================================
    path("cadastrar/fornecedor/", Create_Fornecedor.as_view(), name="novo_fornecedor"),
    path("listar/fornecedor/", List_Fornecedor.as_view(), name="listar_fornecedor"),
    path("editar/fornecedor/<int:pk>/", Update_Fornecedor.as_view(), name="editar_fornecedor"),
    path("excluir/fornecedor/<int:pk>/", Delete_Fornecedor.as_view(), name="excluir_fornecedor"),
    path("detalhes/fornecedor/<int:pk>/", Detail_Fornecedor.as_view(), name="detalhes_fornecedor"),

    # ==========================================================================
    # GÊNEROS
    # ==========================================================================
    path("cadastrar/genero/", Create_Genero.as_view(), name="novo_genero"),
    path("listar/genero/", List_Genero.as_view(), name="listar_genero"),
    path("editar/genero/<int:pk>/", Update_Genero.as_view(), name="editar_genero"),
    path("excluir/genero/<int:pk>/", Delete_Genero.as_view(), name="excluir_genero"),
    path("detalhes/genero/<int:pk>/", Detail_Genero.as_view(), name="detalhes_genero"),
    # Aliases de compatibilidade
    path("cadastrar/genero/legacy/", Create_Genero.as_view(), name="novo_Genero"),
    path("listar/genero/legacy/", List_Genero.as_view(), name="listar_Genero"),

    # ==========================================================================
    # CATEGORIAS
    # ==========================================================================
    path("cadastrar/categoria/", Create_Categoria.as_view(), name="novo_categoria"),
    path("listar/categoria/", List_Categoria.as_view(), name="listar_categoria"),
    path("editar/categoria/<int:pk>/", Update_Categoria.as_view(), name="editar_categoria"),
    path("excluir/categoria/<int:pk>/", Delete_Categoria.as_view(), name="excluir_categoria"),
    path("detalhes/categoria/<int:pk>/", Detail_Categoria.as_view(), name="detalhes_categoria"),

    # ==========================================================================
    # LOCAÇÕES
    # ==========================================================================
    path("cadastrar/locacao/", Create_Locacao.as_view(), name="novo_locacao"),
    path("listar/locacao/", List_Locacao.as_view(), name="listar_locacao"),
    path("editar/locacao/<int:pk>/", Update_Locacao.as_view(), name="editar_locacao"),
    path("excluir/locacao/<int:pk>/", Delete_Locacao.as_view(), name="excluir_locacao"),
    path("detalhes/locacao/<int:pk>/", Detail_Locacao.as_view(), name="detalhes_locacao"),
]