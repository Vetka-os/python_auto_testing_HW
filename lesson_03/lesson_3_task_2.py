from smartphone import Smartphone

catalog = [
    Smartphone("Motorola", "TheBest", "+7900900900"),
    Smartphone("Nokia", "Brick", "+7900800800"),
    Smartphone("Sony", "Clamshell", "+7900700700"),
    Smartphone("Chinese", "WoW", "+7900600600"),
    Smartphone("Beauties", "ByBeauty", "+7900500500"),
]

for i in catalog:
    print(f"{i.brand} - {i.model}. {i.number}")
