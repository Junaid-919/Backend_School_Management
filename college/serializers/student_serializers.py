from rest_framework import serializers
from django.conf import settings
from ..models.students import Student
from ..models.course import Course
from .course_serializers import CourseSerializer


class StudentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model = Student
        fields = '__all__'

    def get_photo_url(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return f"{settings.MEDIA_URL}{obj.photo.name}"
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = CourseSerializer(instance.course).data
        representation['photo_url'] = self.get_photo_url(instance)
        return representation
