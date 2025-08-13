from rest_framework import serializers
from ..models.daily_login import Daily_login



class DailyloginSerializer(serializers.ModelSerializer): # if the data is moving from one place to another then it must be serialized

    class Meta:
        model = Daily_login
        fields = '__all__'


