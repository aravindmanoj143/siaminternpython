from rest_framework import viewsets

from .serializers import ClientSerializer
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('Name')
    serializer_class = ClientSerializer