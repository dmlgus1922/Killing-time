'''
가위 바위 보
'''

def game():
    try:
        game_n = int(input('몇 게임을 하실 건가요?\n'))
    except:
        print('숫자(자연수)만 입력해주세요')
        game()

    win = 0
    lose = 0
    draw = 0

    import random
    import time
    mzb ='묵찌빠'
    gbb = '가위바위보'
    rsp = {'가위':1, '바위':2, '보':3, '찌':1, '묵':2, '빠':3}
    com_gbb = {1:'가위', 2:'바위', 3:'보'}
    com_mzb = {1:'찌', 2:'묵', 3:'빠'}

    for i in range(game_n):
        while True:
            user = input('가위, 바위, 보 중에 하나를 선택하세요\n').strip()
            if user not in '가위 바위 보 묵 찌 빠'.split():
                print('다시 입력해주세요 ㅠ\n')
            else:
                break
        com_num = random.randint(1,3)

        if user in mzb:
            com_s = com_mzb[com_num]
        elif user in gbb:
            com_s = com_gbb[com_num]

        print('가위!', end = ' ')
        time.sleep(0.5)
        print('바위!', end=' ')
        time.sleep(0.5)
        print('보!')
        time.sleep(0.5)
        print()
        print(f'당신: {user} 컴퓨터: {com_s}')

        user_n = rsp[user]

        if user_n == com_num:
            draw += 1
        elif (user_n == 1 and com_num == 3) or (user_n == 2 and com_num == 1) or (user_n == 3 and com_num == 2):
            win += 1
        else:
            lose += 1
        if i != game_n-1:
            print(f'{win}승 {draw}무 {lose}패\n')

    print(f'최종 승패:\n{win}승 {draw}무 {lose}패\n')
    again = input('다시 하시겠습니까?(y/n)\n')
    if again in 'y yes Y YES Yes yEs yES yeS YEs'.split():
        game()
        print()

if __name__ == '__main__':
    game()