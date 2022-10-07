from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    cardName: str
    cardPictureLocation: str
    cardRating: str
    cardRarity: str
    cardElixirCost: int
    cardDescription: str


cr_cards = [
    Card(
        "Skeletons",
        "skeletons.png",
        "90/100",
        "Common",
        1,
        "Three fast, very weak melee fighters. Surround your enemies with this pile of bones!",
    ),
    Card(
        "Musketeer",
        "musky.png",
        "90/100",
        "Rare",
        4,
        "Don't be fooled by her delicately coiffed hair, the Musketeer is a mean shot with her trusty boomstick.",
    ),
    Card(
        "Hog Rider",
        "hog_rider.png",
        "80/100",
        "Rare",
        4,
        "Fast melee troop that targets buildings and can jump over river. He followed the echoing call of 'Hog Riderrrrr' all the way through the Arena doors.",
    ),
    Card(
        "Mini Pekka",
        "mini_pekka.png",
        "90/100",
        "Rare",
        4,
        "The Arena is a certified butterfly-free zone. No distractions for P.E.K.K.A, only destruction.",
    ),
    Card(
        "MegaKnight",
        "mk.png",
        "80/100",
        "Legendary",
        7,
        "He lands with the force of 1,000 mustaches, then jumps from one foe to the next dealing huge area damage. Stand aside!",
    ),
    Card(
        "Pekka",
        "pekka.png",
        "80/100",
        "Epic",
        7,
        "A heavily armoured, slow melee fighter. Swings from the hip, but packs a huge punch.",
    ),
    Card(
        "Barbarian Hut",
        "barbarian_hut.png",
        "10/100",
        "Rare",
        7,
        "Building that periodically spawns Barbarians to fight the enemy. Time to make the Barbarians!",
    ),
    Card(
        "Tornado",
        "tornado.png",
        "100/100",
        "Epic",
        3,
        "Drags enemy troops to its center while dealing damage over time, just like a magnet. A big, swirling, Tornado-y magnet.",
    ),
]
