from django.urls import path
from . import views

urlpatterns = [
    path("", views.StronaGlownaView.as_view(), name="strona-glowna"),
    path("posty", views.PostyView.as_view(), name="strona-postow"),
    path("post/<slug:slug>", views.PojedynczyPostView.as_view(),
         name="strona-postu"),  # /posty/konkretny_post
    path("do-przeczytania", views.DoPrzeczytaniaViw.as_view(), name="do-przeczytania")
]
