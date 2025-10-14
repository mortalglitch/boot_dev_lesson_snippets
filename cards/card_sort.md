This was a fun class.

** Absctraction

```
import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        deck = tuple()
        for suit in self.SUITS:
            for rank in self.RANKS:
                deck = (rank ,suit)
                self.__cards.append(deck)        

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if (len(self.__cards) > 0):
            return self.__cards.pop()
        else: 
            return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
```


```
```
