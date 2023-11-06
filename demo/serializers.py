from rest_framework import serializers

from .models import Weapon


# class WeaponSerializer(serializers.Serializer):
#     name = serializers.CharField()


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name']