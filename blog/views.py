
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FormularzKomentarza
from .models import Post

# funkcja strony głównej


class StronaGlownaView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-data"]
    context_object_name = "najnowsze_posty"

    def get_queryset(self):
        queryset = super().get_queryset()
        dane = queryset[:3]
        return dane


class PostyView(ListView):
    template_name = "blog/wszystkie-posty.html"
    model = Post
    ordering = ["-data"]
    context_object_name = "wszystkie_posty"


class PojedynczyPostView(View):
    def czy_zapisany_post(self, request, post_id):
        zapisane_posty = request.session.get("zapisane_posty")
        if zapisane_posty is not None:
            czy_zapisane_na_pozniej = post_id in zapisane_posty
        else:
            czy_zapisane_na_pozniej = False
        return czy_zapisane_na_pozniej

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "tagi_postu": post.hasztagi.all(),
            "formularz_komentarza": FormularzKomentarza,
            "komentarze": post.komentarze.all().order_by("-id"),
            "zapisane_na_pozniej": self.czy_zapisany_post(request, post.id),
        }
        return render(request, "blog/strona-postu.html", context)

    def post(self, request, slug):
        formularz_komentarza = FormularzKomentarza(request.POST)
        post = Post.objects.get(slug=slug)

        if formularz_komentarza.is_valid():
            komentarz = formularz_komentarza.save(commit=False)
            komentarz.post = post
            komentarz.save()

            return HttpResponseRedirect(reverse("strona-postu", args=[slug]))

        context = {
            "post": post,
            "tagi_postu": post.hasztagi.all(),
            "formularz_komentarza": formularz_komentarza,
            "komentarze": post.komentarze.all().order_by("-id"),
            "zapisane_na_pozniej": self.czy_zapisany_post(request, post.id),
        }
        return render(request, "blog/strona-postu.html", context)


class DoPrzeczytaniaViw(View):
    def get(self, request):
        zapisane_posty = request.session.get("zapisane_posty")

        context = {}

        if zapisane_posty is None or len(zapisane_posty) == 0:
            context["posty"] = []
            context["ma_posty"] = False
        else:
            posty = Post.objects.filter(id__in=zapisane_posty)
            context["posty"] = posty
            context["ma_posty"] = True

        return render(request, "blog/zapisane-posty.html", context)

    def post(self, request):
        zapisane_posty = request.session.get("zapisane_posty")

        if zapisane_posty is None:
            zapisane_posty = []

        post_id = int(request.POST["post_id"])

        if post_id not in zapisane_posty:
            zapisane_posty.append(post_id)
        else:
            zapisane_posty.remove(post_id)

        request.session["zapisane_posty"] = zapisane_posty

        return HttpResponseRedirect("/")
