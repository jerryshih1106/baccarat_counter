""" 牌靴類 """
import random
from collections import deque

class BaccaratShoe:
    """
    百家樂 牌靴
    """
    def __init__(self, num_decks:int=8):
        self.cards = deque()
        self.num_decks = num_decks
        self.refresh_shoe()

    def refresh_shoe(self) -> None:
        """
        洗牌
        """
        single_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.cards = deque(single_deck * self.num_decks)
        random.shuffle(self.cards)

    def draw(self) -> int:
        """
        抽牌
        """
        if len(self.cards) == 0:
            raise Exception("There's no cards in deck")
        card = self.cards.pop()
        return card