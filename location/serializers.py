from rest_framework import serializers
from location import models

class EtiquetteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Etiquette
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article
        fields = '__all__'
        # depth = 1

class FamilleArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FamilleArticle
        fields = '__all__'
