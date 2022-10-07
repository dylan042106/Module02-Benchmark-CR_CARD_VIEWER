from django.shortcuts import render
from app import card_info
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def home_page_view(request):
    cards = card_info.cr_cards
    context = {
        "cards": cards,
    }
    return render(request, "template_homePage.html", context)


def singleCardPageView(request, card_name):
    cards = card_info.cr_cards
    for i in cards:
        if i.cardName == card_name:
            context = {
                "name": i.cardName,
                "rating": i.cardRating,
                "rarity": i.cardRarity,
                "elixirCost": i.cardElixirCost,
                "description": i.cardDescription,
            }
    return render(request, "template_cardPage.html", context)
