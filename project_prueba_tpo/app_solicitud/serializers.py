from rest_framework.serializers import ModelSerializer
from .models import Solicitud

class SolicitudSerializer(ModelSerializer):
    class Meta:
        model = Solicitud
        fields = "__all__"