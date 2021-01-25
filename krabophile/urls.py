from django.urls import include, path
from krabophile import views

urlpatterns = [
    path('', views.KrabophileView.as_view(), name='krabophile'),
]
