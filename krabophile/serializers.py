from rest_framework import serializers
from krabophile import models
from django_restql.mixins import DynamicFieldsMixin


class KrabophileSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.Krabophile
        fields = '__all__'