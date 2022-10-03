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
        "skeletons.jpeg",
        "90%",
        "Common",
        1,
        "Card_description",
    ),
    Card(
        "Electro Spirit",
        "electro_spirit.jpeg",
        "90%",
        "Common",
        1,
        "Card_description",
    ),
    Card(
        "Ice Spirit",
        "ice_spirit.jpg",
        "90%",
        "Common",
        1,
        "Card_description",
    ),
    Card(
        "Fire Spirit",
        "fire_spirit.jpeg",
        "60%",
        "Common",
        1,
        "Card_description",
    ),
    Card(
        "Heal Spirit",
        "heal_spirit.jpg",
        "60",
        "Rare",
        1,
        "Card Description",
    ),
    Card(
        "Mirror",
        "mirror.jpeg",
        "80%",
        "Epic",
        0,
        "Card_description",
    ),
    Card(
        "Goblins",
        "goblins.jpg",
        "50%",
        "Common",
        2,
        "Card_description",
    ),
    Card(
        "Bomber",
        "bomber.jpeg",
        "70%",
        "Common",
        2,
        "Card_description",
    ),
    Card(
        "Spear Goblins",
        "spear_goblins.jpeg",
        "60%",
        "Common",
        2,
        "Card Description",
    ),
    Card(
        "Ice Golem",
        "ice_golem.jpeg",
        "90%",
        "Rare",
        2,
        "Card_description",
    ),
    Card("Bats", "bats.jpg", "70%", "Common", 2, "Card_description"),
    Card("Wall Breakers", "wall_breakers.jpeg", "60%", "Epic", 2, "Card_description"),
    Card("Musketeer", "musky.jpg", "90%", "Rare", 4, "Card_description"),
    Card("Hog Rider", "hog_rider.jpg", "80%", "Rare", 4, "Card_description"),
    Card("Mini Pekka", "mini_pekka.jpg", "90%", "Rare", 4, "Card_description"),
    Card(
        "MegaKnight",
        "megaknight.",
        "80%",
        "Legendary",
        7,
        "Card_description",
    ),
    Card("Pekka", "not available atm", "80%", "Epic", 7, "Card_description"),
    Card(
        "Archer Queen",
        "not available atm",
        "80%",
        "Champion",
        5,
        "Card_description",
    ),
    Card(
        "Cannon",
        "not available atm",
        "90%",
        "Common",
        3,
        "Card Description",
    ),
    Card(
        "Bowler",
        "not available atm",
        "80%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Minion Horde",
        "not available atm",
        "10%",
        "Common",
        5,
        "Card Description",
    ),
    Card(
        "Barbarians",
        "not available atm",
        "20%",
        "Common",
        5,
        "Card Description",
    ),
    Card(
        "Wizard",
        "not available atm",
        "80%",
        "Rare",
        5,
        "Card Description",
    ),
    Card(
        "Prince",
        "not available atm",
        "80%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Fireball",
        "not available atm",
        "100%",
        "Rare",
        4,
        "Card Description",
    ),
    Card(
        "Log",
        "not available atm",
        "100%",
        "Legendary",
        2,
        "Card Description",
    ),
    Card(
        "Zap",
        "not available atm",
        "90%",
        "Common",
        2,
        "Card Description",
    ),
    Card(
        "Skeleton King",
        "not available atm",
        "60%",
        "Champion",
        4,
        "Card Description",
    ),
    Card("Battle Healer", "not available atm", "70%", "Rare", 4, "Card Description"),
    Card("Xbow", "not available atm", "90%", "Epic", 6, "Card Description"),
    Card("Tesla", "not available atm", "100%", "Common", 4, "Card Description"),
    Card("Inferno Tower", "not available atm", "80%", "Rare", 5, "Card Description"),
    Card("Rocket", "not available atm", "80%", "Rare", 6, "Card Description"),
    Card("Lightening", "not available atm", "90%", "Epic", 6, "Card Description"),
    Card(
        "Three Musketeers",
        "not available atm",
        "30%",
        "Rare",
        9,
        "Card Description",
    ),
    Card("Electro Giant", "not available atm", "70%", "Epic", 7, "Card Description"),
    Card("Sparky", "not available atm", "80%", "Legendary", 6, "Card Description"),
    Card(
        "Lava Hound",
        "not available atm",
        "70%",
        "Legendary",
        7,
        "Card Description",
    ),
    Card(
        "Barbarian Hut",
        "not available atm",
        "10%",
        "Rare",
        7,
        "Card Description",
    ),
    Card(
        "Golem",
        "not available atm",
        "70%",
        "Epic",
        8,
        "Card Description",
    ),
    Card(
        "Giant",
        "not available atm",
        "80%",
        "Rare",
        5,
        "Card Description",
    ),
    Card(
        "Elixir Collector",
        "not available atm",
        "50%",
        "Rare",
        6,
        "Card Description",
    ),
    Card("Goblin Giant", "not available atm", "60%", "Epic", 6, "Card Description"),
    Card(
        "Elite Barbarians",
        "not available atm",
        "90%",
        "Common",
        6,
        "Card Description",
    ),
    Card("Valkrie", "not available atm", "80%", "Rare", 4, "Card Description"),
    Card("Minions", "not available atm", "70%", "Common", 3, "Card Description"),
    Card("Princess", "not available atm", "80%", "Legendary", 3, "Card Description"),
    Card("Fire Cracker", "not available atm", "80%", "Common", 3, "Card Description"),
    Card("Giant Skeleton", "not available atm", "80%", "Epic", 6, "Card Description"),
    Card("Clone", "not available atm", "70%", "Epic", 3, "Card Description"),
    Card("Tornado", "not available atm", "100%", "Epic", 3, "Card Description"),
    Card("Goblin Gang", "not available atm", "70%", "Common", 3, "Card Description"),
    Card(
        "Skeleton Barrel",
        "not available atm",
        "80%",
        "Common",
        3,
        "Card Description",
    ),
    Card("Miner", "not available atm", "80%", "Legendary", 3, "Card Description"),
    Card("Bandit", "not available atm", "70%", "Legendary", 3, "Card Description"),
    Card(
        "Royal Ghost",
        "not available atm",
        "60%",
        "Legendary",
        3,
        "Card Description",
    ),
    Card("Fisherman", "not available atm", "80%", "Legendary", 3, "Card Description"),
    Card("Dart Goblin", "not available atm", "90%", "Rare", 3, "Card Description"),
    Card("Goblin Barrel", "not available atm", "90%", "Epic", 3, "Card Description"),
    Card("Mega Minion", "not available atm", "70%", "Rare", 3, "Card Description"),
    Card("Elixir Golem", "not available atm", "80%", "Rare", 3, "Card Description"),
    Card("Tombstone", "not available atm", "80%", "Rare", 3, "Card Description"),
    Card("Arrows", "not available atm", "90%", "Common", 3, "Card Description"),
    Card("Rage", "not available atm", "80%", "Epic", 2, "Card Description"),
    Card(
        "Lumberjack",
        "not available atm",
        "90%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card("Snowball", "not available atm", "80%", "Common", 2, "Card Description"),
    Card(
        "Ice Wizard",
        "not available atm",
        "80%",
        "Legendary",
        3,
        "Card Description",
    ),
    Card(
        "Skeleton Army",
        "not available atm",
        "80%",
        "Epic",
        3,
        "Card Description",
    ),
    Card(
        "Guards",
        "not available atm",
        "80%",
        "Epic",
        3,
        "Card Description",
    ),
    Card(
        "Barbarian Barrel",
        "not available atm",
        "90%",
        "Epic",
        2,
        "Card Description",
    ),
    Card("Earthquake", "not available atm", "90%", "Rare", 3, "Card Description"),
    Card(
        "Royal Delivery",
        "not available atm",
        "90%",
        "Common",
        3,
        "Card Description",
    ),
    Card("Baby Dragon", "not available atm", "60%", "Epic", 4, "Card Description"),
    Card("Dark Prince", "not available atm", "80%", "Epic", 4, "Card Description"),
    Card(
        "Electro Wizard",
        "not available atm",
        "80%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card(
        "Inferno Dragon",
        "not available atm",
        "80%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card(
        "Magic Archer",
        "not available atm",
        "70%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card(
        "Night Witch",
        "not available atm",
        "60%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card("Hunter", "not available atm", "80%", "Epic", 4, "Card Description"),
    Card("Zappies", "not available atm", "50%", "Rare", 4, "Card Description"),
    Card(
        "Mother Witch",
        "not available atm",
        "70%",
        "Legendary",
        4,
        "Card Description",
    ),
    Card(
        "Mortar",
        "not available atm",
        "70%",
        "Common",
        4,
        "Card Description",
    ),
    Card(
        "Flying Machine",
        "not available atm",
        "70%",
        "Rare",
        4,
        "Card Description",
    ),
    Card(
        "Knight",
        "not available atm",
        "90%",
        "Common",
        3,
        "Card Description",
    ),
    Card(
        "Archers",
        "not available atm",
        "70%",
        "Common",
        3,
        "Card Description",
    ),
    Card(
        "Golden Knight",
        "not available atm",
        "80%",
        "Champion",
        4,
        "Card Description",
    ),
    Card(
        "Freeze",
        "not available atm",
        "90%",
        "Epic",
        4,
        "Card Description",
    ),
    Card(
        "Poison",
        "not available atm",
        "80%",
        "Epic",
        4,
        "Card Description",
    ),
    Card(
        "Balloon",
        "not available atm",
        "80%",
        "Epic",
        4,
        "Card Description",
    ),
    Card(
        "Goblin Cage",
        "not available atm",
        "80%",
        "Rare",
        4,
        "Card Description",
    ),
    Card(
        "Mighty Miner",
        "not available atm",
        "80%",
        "Champion",
        4,
        "Card Description",
    ),
    Card(
        "Skeleton Dragons",
        "not available atm",
        "30%",
        "Common",
        14,
        "Card Description",
    ),
    Card(
        "Furnace",
        "not available atm",
        "70%",
        "Rare",
        4,
        "Card Description",
    ),
    Card(
        "Goblin Drill",
        "not available atm",
        "60%",
        "Epic",
        4,
        "Card Description",
    ),
    Card(
        "Bomb Tower",
        "not available atm",
        "70%",
        "Rare",
        4,
        "Card Description",
    ),
    Card(
        "Witch",
        "not available atm",
        "60%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Goblin hut",
        "not available atm",
        "70%",
        "Rare",
        5,
        "Card Description",
    ),
    Card(
        "Cannon Cart",
        "not available atm",
        "80%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Royal Hogs",
        "not available atm",
        "60%",
        "Rare",
        5,
        "Card Description",
    ),
    Card(
        "Rascals",
        "not available atm",
        "70%",
        "Common",
        5,
        "Card Description",
    ),
    Card(
        "Ram Rider",
        "not available atm",
        "70%",
        "Legendary",
        5,
        "Card Description",
    ),
    Card(
        "Electro Dragon",
        "not available atm",
        "80%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Graveyard",
        "not available atm",
        "90%",
        "Legendary",
        5,
        "Card Description",
    ),
    Card(
        "Executioner",
        "not available atm",
        "70%",
        "Epic",
        5,
        "Card Description",
    ),
    Card(
        "Royal Giant",
        "not available atm",
        "80%",
        "Common",
        6,
        "Card Description",
    ),
    Card(
        "Royal Recruits",
        "not available atm",
        "70%",
        "Common",
        7,
        "Card Description",
    ),
]
