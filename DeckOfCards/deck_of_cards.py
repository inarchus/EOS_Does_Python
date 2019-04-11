import random
import math


class CardDeck:
    suits = ['\u2660', '\u2663', '\u2664', '\u2662']
    types = [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self):
        self.card_order = [x + y for x in CardDeck.suits for y in CardDeck.types]
        self.card_map = {card: pos for pos, card in enumerate(self.card_order)}
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.card = self.draw()
        if self.card:
            return self.card
        raise StopIteration

    def __str__(self):
        return ' '.join(self.card_order[self.current:])

    def draw(self):
        self.current += 1
        if self.current <= len(self.card_order):
            return self.card_order[self.current - 1]
        else:
            return None

    def shuffle(self, splits=0, merges=0):
        if not splits and not merges:
            pass
        else:
            pass


deck = CardDeck()

s = ''
for x in deck:
    s += x
print(s)
