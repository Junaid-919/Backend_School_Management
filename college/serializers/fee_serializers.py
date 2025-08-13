from rest_framework import serializers
from ..models.course import Course
from ..models.fee_structure import FeeStructure
from ..models.fee_term import FeeTerm
from ..models.fee_component import FeeComponent
from .fee_term_serializers import FeeTermSerializer



class FeeStructureSerializer(serializers.ModelSerializer):
    terms = FeeTermSerializer(many=True)
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = FeeStructure
        fields = ['id', 'course', 'course_name', 'admission_type', 'academic_year', 'total_fee_amount', 'instance_id', 'terms']

    def create(self, validated_data):
        terms_data = validated_data.pop('terms')
        structure = FeeStructure.objects.create(**validated_data)
        for term_data in terms_data:
            components_data = term_data.pop('components')
            term = FeeTerm.objects.create(fee_structure=structure, **term_data)
            for component_data in components_data:
                FeeComponent.objects.create(fee_term=term, **component_data)
        return structure