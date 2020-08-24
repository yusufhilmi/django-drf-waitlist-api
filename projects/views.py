from rest_framework import generics

from projects.models import Waiter
from projects.serializers import WaiterSerializer


class WaiterCreate(generics.ListCreateAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
