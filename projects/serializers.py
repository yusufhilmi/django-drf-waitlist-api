from rest_framework import serializers
from projects.models import Waiter


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'
