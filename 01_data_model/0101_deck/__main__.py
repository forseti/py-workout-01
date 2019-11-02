from .deck import Card, FrenchDeck
from random import choice

beer_card = Card('7', 'diamonds')
print(f'beer_card: {beer_card}')
print()

print("by implementing '__getitem__' and '__len__', our deck behaves like a list")
deck = FrenchDeck()
print(f'list(deck): {list(deck)}')
print(f'len(deck): {len(deck)}')
print()

print("get a random card using 'random.choice'")
print(f'choice(deck): {choice(deck)}')
print(f'choice(deck): {choice(deck)}')
print(f'choice(deck): {choice(deck)}')
print()

print("get the top 3 cards")
print(f'deck[:3]: {deck[:3]}')
print()

print("get the ace cards, by starting on index 12 and skip 13 cards at a time")
print(f'deck[12::13]: {deck[12::13]}')
print()

print("by implementing '__getitem__', our deck is iterable")
for card in deck:
    print(card)
print()

print("we can reverse our deck with 'reversed'")
for card in reversed(deck):
    print(card)
print()

print(f"Card('Q', 'hearts') in deck: {Card('Q', 'hearts') in deck}")
print(f"Card('7', 'beasts') in deck: {Card('7', 'beasts') in deck}")
print()


print("we can sort the deck by the card ranks")
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

print()



