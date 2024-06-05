class Flower:

    def __init__(self, name, color, freshness, stem_length, cost, lifetime):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost
        self.lifetime = lifetime

    def __repr__(self):
        return (
            f"{self.name}(Color: {self.color}, Freshness: {self.freshness}, Stem-length: {self.stem_length}, "
            f"Cost$: {self.cost}, Lifetime: {self.lifetime} days)"
        )


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifetime):
        super().__init__("Rose", color, freshness, stem_length, cost, lifetime)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifetime):
        super().__init__("Tulip", color, freshness, stem_length, cost, lifetime)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifetime):
        super().__init__("Lily", color, freshness, stem_length, cost, lifetime)


class Daisy(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifetime):
        super().__init__("Daisy", color, freshness, stem_length, cost, lifetime)


class Orchid(Flower):
    def __init__(self, color, freshness, stem_length, cost, lifetime):
        super().__init__("Orchid", color, freshness, stem_length, cost, lifetime)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def average_lifetime(self):
        if not self.flowers:
            return 0
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def search_flowers(self, **kwargs):
        result = self.flowers
        for key, value in kwargs.items():
            result = [flower for flower in result if getattr(flower, key) == value]
        return result

    def __repr__(self):
        return f"Bouquet({self.flowers})"


rose = Rose("Red", 10, 30, 5, 17)
tulip = Tulip('Yellow', 5, 25, 3, 8)
lily = Lily('White', 9, 20, 4, 12)
orchid = Orchid('Blue', 7, 15, 10, 10)
daisy = Daisy('Pink', 12, 17, 17, 15)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)
bouquet.add_flower(orchid)
bouquet.add_flower(daisy)
print(bouquet)

print(f"Average Lifetime of Bouquet: {bouquet.average_lifetime()} days")

bouquet.sort_flowers(key="cost")
print(f"Sorted by cost: {bouquet}")

bouquet.sort_flowers(key="freshness")
print(f"Sorted by freshness: {bouquet}")

bouquet.sort_flowers(key="lifetime")
print(f"Sorted by lifetime: {bouquet}")

bouquet.sort_flowers(key="stem_length")
print(f"Sorted by stem_length: {bouquet}")


search_result = bouquet.search_flowers(color='Pink')
print(f"Flowers with color 'Pink': {search_result}")

search_result = bouquet.search_flowers(lifetime=15)
print(f"Flowers with lifetime 15: {search_result}")
