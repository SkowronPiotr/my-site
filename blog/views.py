from django.shortcuts import render


def strona_glowna(request):
    return render(request, "blog/index.html")


def posty(request):
    pass


def pojedynczy_post(request):
    pass
