from datetime import date
from django.shortcuts import render

wszystkie_posty = [
    {"slug": "wspinaczka-w-gorach",
     "obrazek": "mountains.jpg",
     "autor": "ja",
     "data": date(2023, 11, 22),
     "tytuł": "wspinaczka",
     "opis": "lorem lorem",
     "zawartość": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illum magnam dignissimos neque consequatur sit, odio reprehenderit totam expedita ad ipsa laborum nesciunt deleniti nihil tempore velit iure excepturi. Aperiam, explicabo.",
     },
    {
        "slug": "programming-is-fun",
        "obrazek": "coding.jpg",
        "autor": "Maximilian",
        "data": date(2022, 3, 10),
        "tytuł": "Programming Is Great!",
        "opis": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "zawartość": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "obrazek": "woods.jpg",
        "autor": "Maximilian",
        "data": date(2020, 8, 5),
        "tytuł": "Nature At Its Best",
        "opis": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "zawartość": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

# patrzy na value daty każdego postu


def wyciagnij_date(post):
    return wszystkie_posty["data"]

# funkcja strony głównej


def strona_glowna(request):
    # sortuje posty po najnowszej dacie wskazując na funkcje
    posortowane_posty = sorted(wszystkie_posty, key=wyciagnij_date)
    najnowsze_posty = posortowane_posty[-3:]
    # pobiera 3 ostatnie elementy z listy
    return render(request, "blog/index.html", {
        'najnowsze_posty': najnowsze_posty
    })


def posty(request):
    return render(request, "blog/wszystkie-posty.html")


def pojedynczy_post(request, slug):
    return render(request, "blog/strona-postu.html")
