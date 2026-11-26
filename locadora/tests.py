from django.contrib.auth.models import Group, User
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Categoria, Cliente, Filme, Genero


class OwnedClientRecordTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="senha-forte")
        self.other_user = User.objects.create_user(username="other", password="senha-forte")
        self.owned_client = Cliente.objects.create(
            nome="Cliente do proprietário",
            email="cliente@example.com",
            cpf="111.111.111-11",
            telefone="(11) 11111-1111",
            codigo="OWN-1",
            cadastrado_por=self.owner,
        )
        self.other_client = Cliente.objects.create(
            nome="Cliente de outra pessoa",
            email="outro@example.com",
            cpf="222.222.222-22",
            telefone="(22) 22222-2222",
            codigo="OTHER-1",
            cadastrado_por=self.other_user,
        )
        self.client.login(username="owner", password="senha-forte")

    def test_list_and_detail_only_include_owned_records(self):
        response = self.client.get(reverse("listar_cliente"))

        self.assertContains(response, "Cliente do proprietário")
        self.assertNotContains(response, "Cliente de outra pessoa")
        self.assertEqual(
            self.client.get(reverse("detalhes_cliente", args=[self.other_client.pk])).status_code,
            404,
        )

    def test_other_users_record_cannot_be_updated_or_deleted(self):
        update_response = self.client.get(
            reverse("editar_cliente", args=[self.other_client.pk])
        )
        delete_response = self.client.post(
            reverse("excluir_cliente", args=[self.other_client.pk])
        )

        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)
        self.assertTrue(Cliente.objects.filter(pk=self.other_client.pk).exists())

    def test_create_update_and_delete_show_success_messages(self):
        create_response = self.client.post(
            reverse("novo_cliente"),
            {
                "nome": "Novo cadastro",
                "email": "novo@example.com",
                "cpf": "444.444.444-44",
                "telefone": "(44) 44444-4444",
                "codigo": "NEW-1",
            },
            follow=True,
        )
        self.assertContains(create_response, "Cliente cadastrado com sucesso!")
        new_client = Cliente.objects.get(codigo="NEW-1")
        self.assertEqual(new_client.cadastrado_por, self.owner)

        update_response = self.client.post(
            reverse("editar_cliente", args=[self.owned_client.pk]),
            {
                "nome": "Cliente atualizado",
                "email": self.owned_client.email,
                "cpf": self.owned_client.cpf,
                "telefone": self.owned_client.telefone,
                "codigo": self.owned_client.codigo,
            },
            follow=True,
        )
        self.assertContains(update_response, "Cliente atualizado com sucesso!")

        delete_response = self.client.post(
            reverse("excluir_cliente", args=[new_client.pk]),
            follow=True,
        )
        self.assertContains(delete_response, "Cliente excluído com sucesso!")
        self.assertFalse(Cliente.objects.filter(pk=new_client.pk).exists())

    def test_public_homepage_still_shows_the_catalog_to_visitors(self):
        category = Categoria.objects.create(
            nome="Público",
            prazo_devolucao=30,
            preco="10.00",
            cadastrado_por=self.owner,
        )
        genre = Genero.objects.create(nome="Drama", cadastrado_por=self.owner)
        Filme.objects.create(
            titulo="Catálogo Público",
            duração="90 min",
            ano_lancamento=2020,
            classificacao="L",
            categoria=category,
            genero=genre,
            cadastrado_por=self.owner,
        )
        self.client.logout()

        response = self.client.get(reverse("página_inicial"))

        self.assertContains(response, "Catálogo Público")

    def test_film_forms_and_filters_only_offer_owned_categories_and_genres(self):
        owned_category = Categoria.objects.create(
            nome="Categoria própria",
            prazo_devolucao=30,
            preco="10.00",
            cadastrado_por=self.owner,
        )
        other_category = Categoria.objects.create(
            nome="Categoria alheia",
            prazo_devolucao=30,
            preco="12.00",
            cadastrado_por=self.other_user,
        )
        owned_genre = Genero.objects.create(nome="Gênero próprio", cadastrado_por=self.owner)
        other_genre = Genero.objects.create(nome="Gênero alheio", cadastrado_por=self.other_user)
        staff_group, _ = Group.objects.get_or_create(name="Funcionário")
        self.owner.groups.add(staff_group)

        create_response = self.client.get(reverse("novo_filme"))
        create_form = create_response.context["form"]
        self.assertIn(owned_category, create_form.fields["categoria"].queryset)
        self.assertNotIn(other_category, create_form.fields["categoria"].queryset)
        self.assertIn(owned_genre, create_form.fields["genero"].queryset)
        self.assertNotIn(other_genre, create_form.fields["genero"].queryset)

        list_response = self.client.get(reverse("listar_filme"))
        filter_form = list_response.context["filter"].form
        self.assertIn(owned_category, filter_form.fields["categoria"].queryset)
        self.assertNotIn(other_category, filter_form.fields["categoria"].queryset)
        self.assertIn(owned_genre, filter_form.fields["genero"].queryset)
        self.assertNotIn(other_genre, filter_form.fields["genero"].queryset)

    def test_filter_pagination_keeps_filter_query_parameters(self):
        for number in range(11):
            Cliente.objects.create(
                nome=f"Alvo {number}",
                email=f"alvo{number}@example.com",
                cpf=f"333.333.333-{number:02d}",
                telefone="(33) 33333-3333",
                codigo=f"TARGET-{number}",
                cadastrado_por=self.owner,
            )

        response = self.client.get(reverse("listar_cliente"), {"nome": "Alvo", "page": 1})

        self.assertContains(response, "nome=Alvo&amp;page=2")


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class AccountRecoveryTests(TestCase):
    def test_login_shows_both_recovery_options(self):
        response = self.client.get(reverse("login"))

        self.assertContains(response, reverse("senha_recuperacao"))
        self.assertContains(response, reverse("recuperar_usuario"))

    def test_username_recovery_sends_usernames_to_submitted_email(self):
        User.objects.create_user(
            username="cinema_user",
            password="senha-forte",
            email="conta@example.com",
        )

        response = self.client.post(
            reverse("recuperar_usuario"),
            {"email": "conta@example.com"},
        )

        self.assertRedirects(response, reverse("recuperar_usuario"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("cinema_user", mail.outbox[0].body)

    def test_password_reset_sends_reset_link(self):
        User.objects.create_user(
            username="cinema_user",
            password="senha-forte",
            email="conta@example.com",
        )

        response = self.client.post(
            reverse("senha_recuperacao"),
            {"email": "conta@example.com"},
        )

        self.assertRedirects(response, reverse("senha_recuperacao_enviada"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("/recuperar-senha/", mail.outbox[0].body)
