from ..base.base_baccarat import BaseBaccaratGambler
from ..except_handler import except_decorator, IllegalInputError

CARD_WIN_WEIGHT = {1:-5, 2:-3, 3:-3, 4:3, 5:3, 6:3, 7:3, 8:-3, 9:-5, 10:0, 11:0, 12:0, 13:0} #牌型優勢值
CARD_POINT_WEIGHT = {1:-6, 2:5, 3:-5, 4:-5, 5:-5, 6:-5, 7:5, 8:5, 9:5, 0:-6} #牌點值
BANKER_ADVENTAGE_CARD = {1:1, 2:1, 3:1, 4:0, 5:0, 6:0, 7:0, 8:1, 9:1, 10:0, 11:0, 12:0, 13:0} #莊家優勢牌


class LogicalCardCounting(BaseBaccaratGambler):
    def __init__(self):
        super().__init__()
        self.current_baccarat_time = -1

    def start(self):
        print("--- 有理數算牌 ---")
        if self.current_baccarat_time == -1:
            self._set_init_attribute() # 初始參數設置
            
        cards = self.player_hands + self.banker_hands

        win_weight_value = 0
        adventage_card = 0
        for card in cards:
            win_weight_value += CARD_WIN_WEIGHT[card]
            adventage_card += BANKER_ADVENTAGE_CARD[card]


        # record
        player_count = self._count_card_num(self.player_hands)
        banker_count = self._count_card_num(self.banker_hands)
        if (player_count > banker_count) & (self.decision == '下閒') or (player_count < banker_count) & (self.decision == '下莊'):
            self.win_times += 1
        
        if (player_count == banker_count) and self.play_times > 0 and self.decision != '觀察一把':
            print("和局, 這把不算")
            self.play_times -= 1


        # decision
        logical_value = win_weight_value + CARD_POINT_WEIGHT[banker_count] + (adventage_card * self.middle_card_num)/self.remain_deck

        print("logical_value: ", logical_value)

        if logical_value < 0:
            self.decision = '下閒'
        elif logical_value > 0:
            self.decision = '下莊'
        else:
            self.decision = '觀察一把'

    @except_decorator
    def _set_init_attribute(self):
        try:
            self.current_baccarat_time = int(input('輸入當前總共牌局數量 (莊+閒+和):'))
            self.total_deck = int(input('輸入當廳使用幾副牌:'))
        except Exception as e:
            raise IllegalInputError(e)
        self.remain_deck = self.total_deck - round(self.current_baccarat_time/6, 2) # 6 為百家樂一局的消耗牌數量
        self.middle_card_num = self.total_deck * 4 #一副牌有每四個花色, 四張牌
        print("若遇洗牌, 請重啟程式")

    def _count_card_num(self, card_list):
        ans = 0
        for card in card_list:
            if card > 10:
                card = 0
            ans += card
        return ans % 10