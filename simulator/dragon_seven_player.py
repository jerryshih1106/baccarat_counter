MAPPING_DICT = {"1":1, "2":0, "3":0, "4": -1, "5":-1, "6":-1, "7":-1, "8":2, "9":2, "10": 0}

class DragonSevenPlayer:
    def __init__(self):
        self.bet_flag = False
        self.score = -32
        self.bet_times = 0
        self.win_times = 0
        self.cur_shoe = 0
        self.win_cards = []

    def judge_and_bet(self) -> None:
        if self.score > 0:
            self.bet_times += 1
            self.bet_flag = True

    def counting(self, cards_list:list) -> None:
        for card in cards_list:
            self.score += MAPPING_DICT[str(card)]

    def review_result(self, player_hands:list, banker_hands:list) -> None:
        if self.bet_flag and len(banker_hands) == 3 \
            and sum(player_hands) % 10 < 7 and sum(banker_hands) % 10 == 7:
            self.win_cards.append((player_hands, banker_hands))
            self.win_times += 1
        self.bet_flag = False
    
    def reset_score(self) -> None:
        self.score = -32
        self.cur_shoe += 1

    def report_result(self) -> tuple:
        """
        output:
        win times: int
        bet times: int
        """
        return self.win_times, self.bet_times