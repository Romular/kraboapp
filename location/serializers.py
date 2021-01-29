from rest_framework import serializers
from location import models
from django_restql.mixins import DynamicFieldsMixin

class EtiquetteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.Etiquette
        fields = '__all__'

class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = '__all__'
        # depth = 1

class FamilleArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.FamilleArticle
        fields = '__all__'


class PretSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    en_retard = serializers.BooleanField()

    class Meta:
        model = models.Pret
        fields = '__all__'
        depth = 1