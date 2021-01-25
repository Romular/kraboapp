from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    """
        Champs pour les Salariés
    """
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        """
            Si salarié Cegid, on prend ce nom/prénom.
            Sinon, on prend le nom, prenom enregistré dans l'utilisateur,
            enfin, on prend le login
        """
        return f"{self.first_name} {self.last_name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Utilisateur", related_name="profile", on_delete=models.CASCADE)
