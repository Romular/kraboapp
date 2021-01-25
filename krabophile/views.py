from django.shortcuts import render
from krabophile import serializers
from krabophile import models
from rest_framework import viewsets
from rest_framework import permissions
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q



class KrabophileViewSet(viewsets.ModelViewSet):
    queryset = models.Krabophile.objects.all()
    serializer_class = serializers.KrabophileSerializer

    def get_queryset(self):
        queryset = models.Krabophile.objects.all()
        nomprenom = self.request.query_params.get('nomprenom', None)
        ville = self.request.query_params.get('ville', None)
        actif = self.request.query_params.get('actif', None)

        if actif == "1" or actif == None:
            actif = True
        else:
            actif = False

        if nomprenom is not None:
            queryset = queryset.filter(Q(nom__contains=nomprenom) | Q(prenom__contains=nomprenom))

        if ville is not None:
            queryset = queryset.filter(ville__contains=ville.strip())

        if actif is not None:
            queryset = queryset.filter(actif=actif)
        return queryset


class KrabophileView(TemplateView, LoginRequiredMixin):
    template_name = "krabophile.html"