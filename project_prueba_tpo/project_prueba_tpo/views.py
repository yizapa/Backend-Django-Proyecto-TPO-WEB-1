from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "bloques/index.html"
    extra_context = {
        "titulo_pagina" : "Bienvenidos a mi empresa"
        }
    
class NosotrosPage(TemplateView):
    template_name = "bloques/nosotros.html"
    extra_context = {
        "titulo_pagina" : "NOSOTROS"
        }
    
class ServiciosPage(TemplateView):
    template_name = "bloques/servicios.html"
    extra_context = {
        "titulo_pagina" : "SERVICIOS"
        }
        
class AutogestionPage(TemplateView):
    template_name = "bloques/autogestion.html"
    extra_context = {
        "titulo_pagina" : "Autogestion"
        }