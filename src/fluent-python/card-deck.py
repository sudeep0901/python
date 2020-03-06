import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # print("__getitem__ called")
        return self._cards[position]

    def __getattribute__(self, name):
        return super().__getattribute__(name)


deck = FrenchDeck()

# randomly choosing the card
chc = choice(deck)
print(chc)

# __get__item method implementation makes cards iterable and indexed

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)


print(Card('Q', 'hearts') in deck)

# ranking the deck cards to assign weightage
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]


# sorting cards based on the weighted

for card in sorted(deck, key=spades_high):
    print(card)


class TestBook:
    def __init__(self):
        pass
# bool not defined then it fallbacks to __len
# 0 - False, 1 = True

    # def __bool__(self):
    #     return False

    def __new__(cls):
        print("New called")
        print(dir(cls))

    def __len__(self):
        # return 0
        return 1


if TestBook():
    print("Ye Truty")
else:
    print("Ye Falsy")
