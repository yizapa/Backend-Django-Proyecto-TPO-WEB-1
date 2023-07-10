from rest_framework.viewsets import ModelViewSet
from .models import Solicitud
from .serializers import SolicitudSerializer

class SolicitudViewSet(ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer