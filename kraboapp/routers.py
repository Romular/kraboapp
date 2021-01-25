from rest_framework import routers
from location.views import ArticleViewSet, FamilleArticleViewSet, EtiquetteViewSet
from krabophile.views import KrabophileViewSet


router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'famille_article', FamilleArticleViewSet)
router.register(r'etiquette', EtiquetteViewSet)
router.register(r'krabophile', KrabophileViewSet)