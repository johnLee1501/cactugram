
from rest_framework import serializers

from cactus.models import CactusModel


class CactusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CactusModel
        fields = '__all__'
