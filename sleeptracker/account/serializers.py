from django.contrib.auth.models import User


class UserSerializer(serializer.ModelSerializer):
    sleeps = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        fields['id','usernam', 'sleeps']