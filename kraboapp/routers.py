from rest_framework import routers
from location import views as locationViews
from krabophile import views as krabophileView


router = routers.DefaultRouter()

router.register(r'article', locationViews.ArticleViewSet)
router.register(r'famille_article', locationViews.FamilleArticleViewSet)
router.register(r'etiquette', locationViews.EtiquetteViewSet)
router.register(r'pret', locationViews.PretViewSet)
router.register(r'krabophile', krabophileView.KrabophileViewSet)