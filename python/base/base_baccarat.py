from ..except_handler import except_decorator, IllegalInputError
MAP_DICT = {"A":1 ,"a": 1,"J":11, "j":11, "Q":12, "q":12, "K":13, "k":13, "t":10, "T":10}
MAP_DICT.update({str(i+1): i+1 for i in range(13)})

class BaseBaccaratGambler:
    def __init__(self):
        self.win_times = 0
        self.play_times = 0
        self.total_times = 0
        self.decision = "第一把"
        
    @except_decorator
    def update_hands(self, player_hands, banker_hands):
        '''
        hand = [1~13 t T j J q Q k K a A]
        '''
        self.banker_hands = ['Missing'] #維持同一個type
        self.player_hands = ['Missing']
        self.banker_hands = self._check_and_transform_hand(banker_hands)
        self.player_hands = self._check_and_transform_hand(player_hands)

    def _check_and_transform_hand(self, hands):
        try:
            return [MAP_DICT[s] for s in hands]
        except Exception as e:
            raise IllegalInputError(e)