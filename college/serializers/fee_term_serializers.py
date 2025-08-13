from rest_framework import serializers
from ..models.fee_component import FeeComponent
from ..models.fee_term import FeeTerm
from .fee_component_serializers import FeeComponentSerializer


class FeeTermSerializer(serializers.ModelSerializer):
    components = FeeComponentSerializer(many=True)

    class Meta:
        model = FeeTerm
        fields = ['id', 'name', 'start_date', 'end_date', 'term_amount', 'components']

    def create(self, validated_data):
        components_data = validated_data.pop('components')
        term = FeeTerm.objects.create(**validated_data)
        for component_data in components_data:
            FeeComponent.objects.create(fee_term=term, **component_data)
        return term