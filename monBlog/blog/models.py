from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie,null=True,on_delete=models.SET_NULL,default=1)

    def __str__(self):
        return self.titre