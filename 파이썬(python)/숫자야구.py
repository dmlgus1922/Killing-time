def baseball():
    import random
    import time
    print('숫자야구 게임을 시작합니다!', '컴퓨터가 네 개의 숫자를 생각합니다. ^-^', sep='\n')
    time.sleep(1.3)
    input('숫자를 생각해냈어요! 게임을 시작하려면 엔터를 입력하세요.')
    ui = '''-----------------------------------------------------
0에서 9까지의 서로 다른 숫자 네 개를 입력하세요. ex) 1 2 3 4
-----------------------------------------------------
'''
    com_num = set()
    player_num_list = {}
    while len(com_num) < 4:
        com_num.add(random.randint(1, 9))
    else:
        com_num = list(com_num)
    game = 0
    while True:
        game += 1
        if player_num_list:
            print('\n---------------------------------------------------')
            print('지금까지 입력한 수')
            for key, value in player_num_list.items():
                print(key, value)

        while True:
            try:
                player = list(map(int, input(ui).split()))
                if len(player) != 4:
                    raise
                for num in player:
                    if num < 0 or 9 < num:
                        raise
                break
            except:
                input('네 개의 0~9숫자를 띄어쓰기 하나를 사이에 두고 입력해주세요 ^^;\n(계속하려면 엔터)')

        if player == com_num:
            print(f'정답입니다! {game}회차 성공.')
            while True:
                check = input(f'한 번 더 하시겠습니까?\n(Y/N)\n').lower()
                if check == 'y' or check == 'yes':
                    baseball()
                elif check == 'n' or check == 'no':
                    print('게임 종료.')
                    return
                else:
                    print('올바르게 입력해주세요..')
        ball = 0
        strike = 0
        for i, num in enumerate(player):
            if num == com_num[i]:
                strike += 1
            elif num in com_num:
                ball += 1

        if ball == 0 and strike == 0:
            input('아웃!!\n(계속하려면 엔터)')
            player_num_list[f'{game})'] = f'{player} 아웃'
        else:
            input(f'{ball}볼, {strike}스트라이크!\n(계속하려면 엔터)')
            player_num_list[f'{game})'] = f'{player} {ball}볼, {strike}스트라이크'


if __name__ == '__main__':
    baseball()
