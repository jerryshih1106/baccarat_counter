from python.baccarat_factory import BaccaratFactory 
PRINT_LINE = '==============================================='
if __name__ == '__main__':
    print("=== 小賭怡情 沒有必勝的公式 ===")
    print("可選擇的算牌模式： ['H': 高階算牌, 'L': 有里數算牌] (initial = 高階算牌)")
    baccarat_processor = BaccaratFactory((input('輸入模式(ensemble 考慮開發中):')))
    baccarat_processor = baccarat_processor.process
    while True:
        player_hands = list(map(str, input('輸入上把閒家牌:').split()))
        banker_hands = list(map(str, input('輸入上把莊家牌:').split()))
        print('\x1b[2J\x1b[H') # skip print content
        baccarat_processor.update_hands(player_hands, banker_hands)
        if "Missing" in baccarat_processor.player_hands or "Missing" in baccarat_processor.banker_hands:
            print(PRINT_LINE)
            continue
        baccarat_processor.start()
        print(PRINT_LINE)
        print(f"第 {baccarat_processor.total_times} 把")
        print("")
        print(f"*** 建議 {baccarat_processor.decision} ***")
        print("")
        print("")
        print(f'勝利次數: {baccarat_processor.win_times}')
        print(f'下注次數: {baccarat_processor.play_times}')
        if baccarat_processor.play_times > 0:
            print(f'Win Rate: {round(baccarat_processor.win_times / baccarat_processor.play_times * 100, 2)}%')
        if baccarat_processor.decision != '觀察一把':
            baccarat_processor.play_times += 1
        baccarat_processor.total_times += 1
        print(PRINT_LINE)

