from django.urls import path
from . import views

urlpatterns = [
    path("", views.strona_glowna, name="strona-glowna"),
    path("posty", views.posty, name="strona-postow"),
    path("post/<slug:slug>", views.pojedynczy_post,
         name="strona-postu"),  # /posty/konkretny_post
]
