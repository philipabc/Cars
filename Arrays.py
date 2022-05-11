import random
deck = list(range(1, 55))
# print(deck)
random.shuffle(deck)

print(deck)

hand = random.sample(deck, k=54)
# print(hand)

print(sorted(hand, reverse=True))

print("This is the highest number", max(hand))
print("This is the lowest number", min(hand))
