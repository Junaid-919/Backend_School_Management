from rest_framework import serializers
from ..models.fee_component import FeeComponent

class FeeComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeComponent
        fields = ['id', 'name', 'amount']