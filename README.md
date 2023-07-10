-- Instalar las dependencias de un archivo de texto. requeriments.txt

    $ pip install -r requirements.txt

-- Creamos nuestro proyecto con django:

    $ django-admin startproject solicitud .


-- Iniciar el Servidor:

    $ python manage.py runserver <PORT a eleccion>(por default es 8000)


-- Generacion app, se utiliza el nombre de app_solicitud, pues se realizara un CRUD

    $ python manage.py startapp app_solicitud

-- Generacion Model:
   /project_prueba_tpo/models.py

    class Solicitud(models.Model):
     	"""
       	Atributos de clase que son usadas por herencia de la clase Model
       	"""
        mensaje = models.CharField(max_length=200)
        prioridad = models.PositiveSmallIntegerField(blank=False, null=False)
        pto = models.FloatField(blank=True, null=True)
	hora = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
	actualizado = models.DateTimeField(auto_now=True, blank=True)

       	# podemos crear la tabla con un nombre especifico pero se lo tenemos
       	# que indicar directamente en la metaclase

        class Meta:
        db_table = "solicitud_table"

        def __str__(self):
            return f"La solicitud: {self.mensaje}, Prioridad {self.prioridad}"

        def get_fields(self):
            return [
                (field.verbose_name, field.value_from_objects(self))
                for field in self.__class__._meta.fields[1:]
            ]

-- Registrar de manera local en la app, en el archivo de app_solicitud/admin.py

 	!No olvidar importar clase Solicitud

	from .models import Solicitud

	@admin.register(Solicitud)
	class SolicitudAdmin(admin.ModelAdmin):
    	...

-- Crear lista APPS = [] en settings.py del proyecto

         APPS = [\
		"app_solicitud"\
		]

	INSTALLED_APPS = [\
    			   'django.contrib.admin',\
    			   'django.contrib.auth',\
                           'django.contrib.contenttypes',\
    			   'django.contrib.sessions',\
    			   'django.contrib.messages',\
    			   'django.contrib.staticfiles'\,
			 ]

	INSTALLED_APPS += APPS

-- Crear la base de datos y hacer las migraciones respectivas

    	$ python manage.py makemigrations
    	$ python manage.py migrate

   Al generar estas migraciones podemos llegar a observar que el archivo sqlite3 tiene las tablas creadas por medio de esa migracion.


-- Generar el usuario y logrando acceder al admin de django

    	$ python manage.py createsuperuser

   		Username: admin\
   		Email address: admin@lfj.com\
   		Password: *************\

   Accedemos al path : http://127.0.0.1:8000/admin

#-------------------------------------------------------#

# -- INTEGRACION CON EL FRONT-END


   Integrar las views, urls y templates, para gestionar nuestro CRUD


   -- Crear archivo urls, para hacer uso de las rutas que genera esta app, dentro de la carpeta de app_solicitud

        $ touch urls.py

   -- Creamos las views, la cuales manjearn la siguiente logicas de creacion, modificacion, actualizacion, borrado y muestra de todos los registros, solicitudes y detalles.

        views.py

            from django.shortcuts import render
            from django.urls import reverse_lazy
            from django.views import View

            from django.views.generic.list import ListView
            from django.views.generic.edit import DeleteView, UpdateView, CreateView
            from django.views.generic.detail import DetailView

            from .models import Solicitud

 	     //# Create your views here.


            class SolicitudBaseView(View):
                template_name = 'solicitud.html'
                model = Solicitud
                fields = '__all__'
                success_url = reverse_lazy('solicitud:all')

            class SolicitudListView(SolicitudBaseView,ListView):
   	        """
   		ESTO ME PERMITE CREAR UNA VISTA CON LAS SOLICTUDES
   		"""

            class SolicitudDetailView(SolicitudBaseView,DetailView):
                template_name = "solicitud_detail.html"

            class SolicitudCreateView(SolicitudBaseView,CreateView):
                template_name = "solicitud_create.html"
                extra_context = {
                    "tipo": "Crear solicitud"
                }


            class SolicitudUpdateView(SolicitudBaseView,UpdateView):
                template_name = "solicitud_update.html"
                extra_context = {
                    "tipo": "Actualizar solicitud"
                }

            class SolicitudDeleteView(SolicitudBaseView,DeleteView):
                template_name = "solicitud_delete.html"
                extra_context = {
                    "tipo": "Borrar solicitud"
                }

   -- Generar las rutas en el archivo urls.py, de tal forma que vamos a indicarle los lugares a donde estaria ingresando desde el front.

        urls.py

            from django.urls import path
            from .router import router


            from .views import      SolicitudListView   \
                                ,   SolicitudDetailView \
                                ,   SolicitudCreateView \
                                ,   SolicitudUpdateView \
                                ,   SolicitudDeleteView

            app_name = "solicitud"

            urlpatterns = [
                path("", SolicitudListView.as_view(), name="all"),
                path("create/", SolicitudCreateView.as_view(), name="create"),
                path("<int:pk>/detail/", SolicitudDetailView.as_view(), name="detail"),
                path("<int:pk>/update/", SolicitudUpdateView.as_view(), name="update"),
                path("<int:pk>/delete/", SolicitudDeleteView.as_view(), name="delete")

            ]

            urlpatterns += router.urls

   -- Verifiquemos algunos de los archivos de la carpeta templates de la app, por ejemplo : solicitud_create.html

        {% extends 'base_solicitud.html' %}
        {% block content %}

        <main>
            <div class="main-color-solicitud">
                <h1>CREAR SOLICITUD</h1>
                <form method="post">
                    {% csrf_token %}
                    <div>{{form.as_p}}</div>
                    <input type="submit" value="{{ tipo }}" />
                </form>

                <a href="{% url 'solicitud:all' %}">Volvamos al Inicio</a>
            </div>
        </main>
        {% endblock %}

   -- Integrar a la ruta del proyecto como lo indicamos en el siguiente archivo:

   	/project_prueba_tpo/urls.py

        from django.contrib import admin
        from django.urls import path, include
        from .views import IndexPage, NosotrosPage, ServiciosPage, AutogestionPage

        urlpatterns = [
            path("admin/", admin.site.urls),
            path('', IndexPage.as_view(), name="index_page"),
            path('nosotros/', NosotrosPage.as_view(), name="nosotros_page"),
            path('servicios/', ServiciosPage.as_view(), name="servicios_page"),
            path('autogestion/', AutogestionPage.as_view(), name="autogestion_page"),
            path('solicitud/', include('app_solicitud.urls')),
        ]


# -- Creacion de una API rest utilizando django-rest-framework

   -- En esta integracion, para generar una api con un modulo que se llama rest_framework, para la cual necesitamos instalar la siguiente dependecia django_rest_framework:

            $ pip install djangorestframework


   -- Al integrarlo vamos a trabajar en unos modulos que deberan tener el siguiente formato, pues son los que integra lo necesario del paquete.

   serializers.py : esto realiza una transformacion de los registros en un formato del tipo json, que va a ser la respuesta de la api

        from rest_framework.serializers import ModelSerializer
        from .models import Solicitud

        class SolicitudSerializer(ModelSerializer):
            class Meta:
                model = Solicitud
                fields = "__all__"

   viewsets.py : estos me permite tener unas vistas direccionadas al modelo junto con el queryset determinado

        from rest_framework.viewsets import ModelViewSet
        from .models import Solicitud
        from .serializers import SolicitudSerializer

        class SolicitudViewSet(ModelViewSet):
            queryset = Solicitud.objects.all()
            serializer_class = SolicitudSerializer

   router.py : Esto me genera las rutas que van a integrarse a los paths de los que vaya a indicarle, en este caso sera de la siguiente forma.

        from rest_framework import routers
        from .viewsets import SolicitudViewSet

        router = routers.SimpleRouter()

   //# en este caso se le anexa a la ruta de las urls de la app
        router.register("api-solicitud",SolicitudViewSet)

   -- Es importante colocar la app de rest_framework en los settings.

               # Application definition

                APPS = [
                    "app_solicitud"
                ]

                EXTERNALS = [
                    "rest_framework"
                ]

                INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                ]


                INSTALLED_APPS += APPS
                INSTALLED_APPS += EXTERNALS

   -- ya podemos acceder a la ruta :

   http://127.0.0.1:8000/solicitud/api-solicitud/

#------------------------------------------------------#

#REFERENCIAS

 Clases Curso FullStack Python Codo a codo 4.0 - Profesor: Anderson Ocaña -
