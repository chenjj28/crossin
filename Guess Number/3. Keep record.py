#统计游戏数据：玩家姓名、总游戏次数（玩家每猜中答案算玩了一次游戏）、
#总游戏轮数（玩家每猜一个数字算玩了一轮游戏）、最快猜中轮数，并将结果保存在文件中

import random

name = input('Please enter your name: ')
game_times = 0                              #总游戏次数
min_round = 0                               #最快猜中轮数
total_round = 0                             #总游戏轮数
play = 'Y'
while play == 'Y':
    game_times += 1
    this_round = 0                          #每次游戏猜的轮数
    num = random.randint(1, 100)
    bingo = False
    while bingo == False:
        answer = int(input("Input a number between 1 to 100: "))
        this_round += 1
        if answer > num:
            print('Too big')
        elif answer < num:
            print('Too small')
        else:
            print('Bingo!')
            bingo = True
    total_round += this_round               #每轮游戏用的轮数加入到总轮数中
    if min_round == 0 or this_round < min_round:           #首次游戏或本次游戏猜对轮数小于之前最小轮数
        min_round = this_round
    print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
          % (name, game_times, min_round, total_round / game_times))
    play = input('Do you want to continue? Y to continue, others to quit.')
    
result = f'{name} {game_times} {min_round} {total_round}'          #整理记录

with open('game_one_user.txt', 'w') as f:
    f.writelines(result)                                           #将记录写入文件
