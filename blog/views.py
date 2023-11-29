
from django.shortcuts import render, get_object_or_404
from .models import Post


# funkcja strony głównej


def strona_glowna(request):
    # sortuje posty po najnowszej dacie wskazując na funkcje
    najnowsze_posty = Post.objects.all().order_by("-data")[:3]
    return render(request, "blog/index.html", {
        'najnowsze_posty': najnowsze_posty
    })


def posty(request):
    wszystkie_posty = Post.objects.all().order_by("-data")
    return render(request, "blog/wszystkie-posty.html", {
        "wszystkie_posty": wszystkie_posty,
    })


def pojedynczy_post(request, slug):
    zindentyfikowany_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/strona-postu.html", {
        "zindentyfikowany_post": zindentyfikowany_post,
        "tagi_postu": zindentyfikowany_post.hasztagi.all()
    })
