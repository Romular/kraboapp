from django.urls import include, path
from location import views

urlpatterns = [
    path('etiquette/pdf/<int:count>/', views.etiquette_print_pdf, name='etiquette_print_pdf'),
    path('article/', views.ArticleView.as_view(), name="gestion_article"),
    path('pret/', views.PretView.as_view(), name="pret"),
    # path('etiquette/html/', views.etiquette_print_html, name='etiquette_print_html'),
]
