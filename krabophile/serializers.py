from rest_framework import serializers
from krabophile import models

class KrabophileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Krabophile
        fields = '__all__'