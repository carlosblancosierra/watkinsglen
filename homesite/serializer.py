from .models import Homesite
from rest_framework import serializers

class HomesiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homesite
        fields = '__all__'
