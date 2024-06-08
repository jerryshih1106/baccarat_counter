from python.baccarat_factory import BaccaratFactory 

if __name__ == '__main__':
    print("=== 小賭怡情 沒有必勝的公式 ===")
    print("可選擇的算牌模式： ['HighLevelCounting'] (initial = HighLevelCounting)")
    baccarat_processor = BaccaratFactory((input('輸入模式(ensemble 考慮開發中):')))
    baccarat_processor = baccarat_processor.process
    while True:
        player_hands = list(map(str, input('輸入上把閒家牌:').split()))
        banker_hands = list(map(str, input('輸入上把莊家牌:').split()))
        baccarat_processor.update_hands(player_hands, banker_hands)
        baccarat_processor.start()
    
        print(f"*** 建議 {baccarat_processor.decision} ***")
        print(f'勝利次數: {baccarat_processor.win_times}')
        print(f'總次數: {baccarat_processor.total_times}')
        if baccarat_processor.total_times > 0:
            print(f'Win Rate: {baccarat_processor.win_times / baccarat_processor.total_times * 100}%')
        if baccarat_processor.decision != '觀察一把':
            baccarat_processor.total_times += 1
        print('===============================================')

