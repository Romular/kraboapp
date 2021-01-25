from django.db import models
from django.utils import timezone


# Create your models here.

class Krabophile(models.Model):

    """
        Un Krabophile est un utilisateur du krabo.
        Cet objet est nécessaire pour louer ou emprunter, et suivre l'état des pret et locations
    """
    # Nom et prénom
    prenom = models.CharField("Nom", null=False, blank=False, max_length=150, db_index=True) 
    nom = models.CharField("Nom", null=False, blank=False, max_length=150, db_index=True)
    # Première ligne de l'adresse
    adresse = models.CharField("Adresse", null=False, blank=False ,max_length=250)
    # Seconde ligne de l'adresse, optionnelle
    adresse_complement = models.CharField("Adresse (complément)", null=False, blank=True, max_length=250, default="")
    # Code Postal
    code_postal = models.CharField("Code Postal", null=False, blank=False, max_length=10, default="", db_index=True)
    # Ville, avec CEDEX si besoin
    ville = models.CharField("Ville", null=False, blank=False, max_length=150, db_index=True)
    # Est ce que c'est un sociétaire ?
    societaire = models.BooleanField("Sociétaire", default=False, db_index=True)
    # Actif ?
    actif = models.BooleanField("Sociétaire", default=True, db_index=True)

    # Date de création
    created = models.DateTimeField(auto_now_add=True)
    # Date de dernière modification
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.prenom} {self.nom}"
