from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    hasztag = models.CharField(max_length=20)

    def __str__(self):
        return self.hasztag

    class Meta:
        verbose_name_plural = "Tagi"


class Autor(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.imie} {self.nazwisko}"

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name_plural = "Autorzy"


class Post(models.Model):
    tytul = models.CharField(max_length=150)
    zawartosc = models.CharField(max_length=200)
    tresc = models.TextField(validators=[MinLengthValidator(10)])
    nazwa_obrazka = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    hasztagi = models.ManyToManyField(Tag, null=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.SET_NULL, null=True, related_name="posty")

    class Meta:
        verbose_name_plural = "Posty"
