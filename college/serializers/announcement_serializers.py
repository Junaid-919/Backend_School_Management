from rest_framework import serializers
from ..models.announcements import Announcement

class AnnouncementSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized

    class Meta:
        model = Announcement
        fields = '__all__'