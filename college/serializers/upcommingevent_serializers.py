from rest_framework import serializers
from ..models.upcommingevent import UpcomingEvent

class UpcomingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvent
        fields = ['id', 'title', 'description', 'event_date']