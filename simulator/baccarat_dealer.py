""" 百家樂 荷官 """
import random
from .baccarat_shoe import BaccaratShoe

class BaccaratDealer:
    def __init__(self, decks_num:int = 8):
        self.decks_num = decks_num
        self.run_shoe_num = 0
        self.shoe = None
        self.game_num = 0
        self.shoe_num = 0
        

    def deal_new_game(self) -> None:
        """
        新的牌局
        """
        self.game_num = 0
        self.shoe_num += 1
        self.shoe = BaccaratShoe(self.decks_num)
        #紅牌
        self.flag = int(len(self.shoe.cards) * random.uniform(0.1, 0.4))


    def _calculate_score(self, hand:list) -> int:
        return sum(hand) % 10

    def _should_banker_draw(self, banker_score:int, player_third_card:int) -> bool:
        """
        莊家補牌規則
        """
        if banker_score >= 7:
            return False
        elif banker_score <= 2:
            return True
        elif banker_score == 3 and player_third_card != 8:
            return True
        elif banker_score == 4 and player_third_card in [2, 3, 4, 5, 6, 7]:
            return True
        elif banker_score == 5 and player_third_card in [4, 5, 6, 7]:
            return True
        elif banker_score == 6 and player_third_card in [6, 7]:
            return True
        return False

    def play_baccarat(self):
        """
        要先有牌靴才能夠玩百家樂
        """
        # 檢查有沒有牌靴, 是否到紅牌了
        if self.shoe is None or self.flag > len(self.shoe.cards) or \
            len(self.shoe.cards) < 6:
            self.deal_new_game()
            return self.play_baccarat()
        self.game_num += 1
        
        player = []
        banker = []
        # 各抽兩次
        for _ in range(2):
            player_card = self.shoe.draw()
            banker_card = self.shoe.draw()
            player.append(player_card)
            banker.append(banker_card)
        
        player_score = self._calculate_score(player)
        banker_score = self._calculate_score(banker)

        # 補牌
        player_third_card = None
        # 玩家補牌
        if player_score <= 5 and banker_score < 8:
            player_third_card = self.shoe.draw()
            player.append(player_third_card)
            player_score = self._calculate_score(player)
        
        # 莊家補牌
        # 1. 當閒沒有補牌, 閒家 <= 7 點 而且 莊家 <= 5 點時要補牌
        # 2. 當閒家有補牌 而且符合莊家補牌規則時補牌
        if (player_third_card is None and player_score <= 7 and banker_score <= 5) or \
            player_third_card is not None and self._should_banker_draw(banker_score, player_third_card):
            banker_third_card = self.shoe.draw()
            banker.append(banker_third_card)
            banker_score = self._calculate_score(banker)
        
        # print(f"第 {self.shoe_num} 副牌靴, 第 {self.game_num} 局")
        # print(f"閒家牌: {player}, 分數: {player_score}")
        # print(f"莊家牌: {banker}, 分數: {banker_score}")
        
        if player_score > banker_score:
            return "閒家贏", player, banker
        elif banker_score > player_score:
            return "莊家贏", player, banker
        else:
            return "和局", player, banker