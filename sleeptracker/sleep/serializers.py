from rest_framework import serializers
from sleep.models import Sleep


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ['id', 'owner', 'created', 'sleep_duration', 'wake_up_time']
        read_only_fields = ['owner', 'created']