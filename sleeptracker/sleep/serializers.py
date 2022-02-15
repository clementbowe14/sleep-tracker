from rest_framework import serializers
from sleep.models import Sleep


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = '__all__'
        read_only_fields = ['owner', 'created']