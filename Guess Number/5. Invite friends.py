#进入游戏时，输入玩家昵称，按玩家昵称读取之前的游戏数据。
#结束游戏后，根据玩家昵称，保存玩家的游戏数据到文本

import random

name = input('Please enter your name: ')

with open('game_many_user.txt') as f:
    lines = f.readlines()
scores = {}                                             #新建一个空字典用来储存成绩
for l in lines:
    record = l.split()                                  #每一行的成绩按空格分隔并组成一个list
    scores[record[0]] = record[1:]                      #写入字典，名字作为key，成绩作为value

if scores.get(name) == None:
    scores[name] = [0, 0, 0]
game_times = int(scores[name][0])                       #总游戏次数
min_round = int(scores[name][1])                        #最快猜中轮数
total_round = int(scores[name][2])                      #总游戏轮数

if game_times > 0:
    ave_round = total_round / game_times
else:
    ave_round = 0

print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
      % (name, game_times, min_round, ave_round))

play = 'Y'
while play == 'Y':
    game_times += 1
    this_round = 0                                      #每次游戏猜的轮数
    num = random.randint(1, 10)
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
    total_round += this_round                           #每轮游戏用的轮数加入到总轮数中
    if min_round == 0 or this_round < min_round:        #首次游戏或本次游戏猜对轮数小于之前最小轮数
        min_round = this_round
    print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
          % (name, game_times, min_round, total_round / game_times))
    play = input('Do you want to continue? Y to continue, others to quit.')

scores[name] = [str(game_times), str(min_round), str(total_round)]      #修改字典中的记录

result = ''                                             #新建一个空字符串
for i in scores:                                        #遍历字典
    line = i + ' ' + ' '.join(scores[i]) + '\n'         #将列表形式的value以join方法变成字符串并与key拼接
    result += line                                      #将每一行的内容拼接成字符串

with open('game_many_user.txt', 'w') as f:
    f.writelines(result)                                #将记录写入文件
