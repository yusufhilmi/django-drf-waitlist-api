from rest_framework import viewsets

from projects.models import Waiter
from projects.serializers import WaiterSerializer


class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
