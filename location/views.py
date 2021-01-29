from django.shortcuts import render
from location import serializers
from location.models import Article, Etiquette, FamilleArticle, Pret
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from io import BytesIO
import tempfile



class EtiquetteViewSet(viewsets.ModelViewSet):
    queryset = Etiquette.objects.all()
    serializer_class = serializers.EtiquetteSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        etiquette = self.request.query_params.get('etiquette', None)
        libelle = self.request.query_params.get('libelle', None)
        famille_id = self.request.query_params.get('famille', None)

        try:
            etiquette = int(etiquette)
        except (ValueError, TypeError):
            etiquette = None

        try:
            famille_id = int(famille_id)
        except (ValueError, TypeError):
            famille_id = None


        if etiquette is not None:
            queryset = queryset.filter(etiquette__id=etiquette)

        if libelle is not None:
            queryset = queryset.filter(libelle__contains=libelle.strip())

        if famille_id is not None:
            queryset = queryset.filter(famille__id=famille_id)
        return queryset


class FamilleArticleViewSet(viewsets.ModelViewSet):
    queryset = FamilleArticle.objects.all()
    serializer_class = serializers.FamilleArticleSerializer

class PretViewSet(viewsets.ModelViewSet):
    queryset = Pret.objects.all()
    serializer_class = serializers.PretSerializer

class ArticleView(LoginRequiredMixin, TemplateView):
    template_name = "article.html"

class PretView(LoginRequiredMixin, TemplateView):
    template_name = "pret.html"

@login_required
def etiquette_print_pdf(request, count):
    """
        Crée une feuille d'étiquettes, et génères les étiquettes correspondantes
        on fait 4x10 etiquettes
    """
    template = "etiquette_pdf.html"
    etiquette_list = Etiquette.create_n_etiquette(count)
    for etiquette in etiquette_list:
        print(etiquette.id)

    context = {
        "etiquette_list": etiquette_list
    }
    return render(request, template, context)

    """
    html_string = render_to_string(template, context)
    html = HTML(string=html_string)
    in_memory_pdf = BytesIO(html.write_pdf())
    pdf = in_memory_pdf.getvalue()
    in_memory_pdf.close()

    response = HttpResponse(content_type='application/pdf; charset=utf-8')
    response['Content-Disposition'] = 'inline; filename=releve.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    response.write(pdf)
    # response['Content-Transfer-Encoding'] = 'binary'
    return response
    """
