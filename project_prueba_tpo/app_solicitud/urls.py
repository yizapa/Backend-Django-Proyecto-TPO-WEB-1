# from django.contrib import admin
# from django.urls import path , include
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
