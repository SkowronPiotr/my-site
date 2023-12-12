from django import forms

from .models import Komentarz


class FormularzKomentarza(forms.ModelForm):
    class Meta:
        model = Komentarz
        exclude = ["post"]
        labels = {
            "nazwa_uzytkownika": "Twoje imię",
            "mail_uzytkownika": "Twój mail",
            "text": "Twój komentarz",
        }
