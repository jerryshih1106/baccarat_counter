from ..base.base_baccarat import BaseBaccaratGambler

WEIGHT = {1:1, 2:1, 3:2, 4:2, 5:2, 6:2, 7:-5, 8:-5, 9:-5, 10:0, 11:0, 12:0, 13:0}
COEF = {0:0, 1:0.1, 2:0.4, 3:0.4, 4:0.4, 5:0.5, 6:0.6, 7:0.7, 8:0.6, 9:0.5}

class HighLevelCounting(BaseBaccaratGambler):
    def __init__(self):
        super().__init__()
        
    def start(self):
        cards = self.player_hands + self.banker_hands
        player_coef, player_count = self._count_coef(self.player_hands)
        banker_coef, banker_count = self._count_coef(self.banker_hands)

        if (player_count > banker_count) & (self.decision == '下閒') or (player_count < banker_count) & (self.decision == '下莊'):
            self.win_times += 1
        
        if (player_count == banker_count) and self.play_times > 0:
            print("和局, 這把不算")
            self.play_times -= 1

        res = 0
        for card in cards:
            res += WEIGHT[card]

        if res * player_coef > res * banker_coef:
            self.decision = '下閒'
        elif res * player_coef < res * banker_coef:
            self.decision = '下莊'
        else:
            self.decision = '觀察一把'

    def _count_coef(self, card_list):
        ans = 0
        for card in card_list:
            if card > 10:
                card = 0
            ans += card
        return COEF[ans % 10], ans % 10

