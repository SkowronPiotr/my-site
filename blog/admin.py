from django.contrib import admin
from .models import Tag, Autor, Post, Komentarz

# piotr djangoblog
# haslo123


class PostAdmin(admin.ModelAdmin):
    list_filter = ("autor", "hasztagi", "data")
    list_display = ("tytul", "data", "autor")
    prepopulated_fields = {"slug": ("tytul",)}


class KomentarzAdmin(admin.ModelAdmin):
    list_display = ("nazwa_uzytkownika", "post")


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Autor)
admin.site.register(Komentarz, KomentarzAdmin)
