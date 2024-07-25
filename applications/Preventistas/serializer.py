from rest_framework import serializers

from .models import Preventista

class PreventistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preventista
        fields = ('__all__')