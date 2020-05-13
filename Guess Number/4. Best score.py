#进入游戏时，从文件读取历史游戏记录，并将游戏数据赋值给一个字典

import random

with open('game_one_user.txt') as f:
    lines = f.readlines()
scores = {}                                             #新建一个空字典用来储存成绩
for l in lines:
    record = l.split()                                  #每一行的成绩按空格分隔并组成一个list
    scores[record[0]] = record[1:]                      #写入字典，名字作为key，成绩作为value
name = record[0]
game_times = int(record[1])                             #总游戏次数
min_round = int(record[2])                              #最快猜中轮数
total_round = int(record[3])                            #总游戏轮数

print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
      % (name, game_times, min_round, total_round / game_times))

play = 'Y'
while play == 'Y':
    game_times += 1
    this_round = 0                                      #每次游戏猜的轮数
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
    total_round += this_round                              #每轮游戏用的轮数加入到总轮数中
    if min_round == 0 or this_round < min_round:           #首次游戏或本次游戏猜对轮数小于之前最小轮数
        min_round = this_round
    print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
          % (name, game_times, min_round, total_round / game_times))
    play = input('Do you want to continue? Y to continue, others to quit.')

result = f'{name} {game_times} {min_round} {total_round}'          #整理记录

with open('game_one_user.txt', 'w') as f:
    f.writelines(result)                                   #将记录写入文件
