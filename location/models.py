from django.db import models
from django.utils import timezone
from krabophile.models import Krabophile



class Etiquette(models.Model):
    """
        Etiquette, a coller sur les livres, jeux ou autres produits en prêt ou location
    """
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return str(self.id)
    
    @staticmethod
    def create_n_etiquette(quantity):
        """
            Crée quantity etiquettes, et les retourne sous forme d'array
        """
        ret = []
        for cpt in range(quantity):
            e = Etiquette()
            e.save()
            ret.append(e)
        return ret



class FamilleArticle(models.Model):
    """
        Famille des articles : Jeux, Livres, etc...
    """
    libelle = models.CharField("Libelle", max_length=50, null=False, blank=False, db_index=True)
    duree_pret = models.IntegerField("Duree pret / loca (j)", null=True, blank=False, db_index=True)

    class Meta:
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Article(models.Model):
    """
        Tous les articles.
    """

    libelle = models.CharField("Nom", max_length=50, null=False, blank=False, db_index=True)
    famille = models.ForeignKey("FamilleArticle", null=False, blank=False, db_index=True, on_delete=models.CASCADE)
    etiquette = models.OneToOneField("Etiquette", null=True, blank=True, db_index=True, on_delete=models.CASCADE, related_name="article")
    # created = models.DateTimeField("Date de Création", db_index=True, editable=False)
    prix_facture_si_non_rendu = models.FloatField("Prix si non rendu", null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["etiquette__id"]

    
    """
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        super().save(*args, **kwargs)
    """

    def __str__(self):
        return self.libelle


class Pret(models.Model):
    """
        Une personne prend un article en pret ou location
    """
    article = models.ForeignKey("Article", null=False, blank=False, db_index=True, on_delete=models.CASCADE)
    krabophile = models.ForeignKey(Krabophile, null=False, blank=False, db_index=True, on_delete=models.CASCADE)
    prix_location = models.FloatField("Prix", null=False, blank=True, db_index=True, default=0)
    # Si pas rendu a date_restitution, sera facturé au prix article.prix_facture_si_non_rendu
    date_restitution = models.DateTimeField("A rendre avant le", db_index=True, null=False)
    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
