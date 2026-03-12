from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "locadora/index.html"

class Sobre(TemplateView):
    template_name = "locadora/sobre.html"

class Contato(TemplateView):
    template_name = "locadora/contato.html"