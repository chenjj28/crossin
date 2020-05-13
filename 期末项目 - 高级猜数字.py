import requests
import random

#定义一次游戏的函数，返回本次游戏猜了几轮
def guess_one():
    this_round = 0  # 每次游戏猜的轮数
    try:                                                            #尝试读取网络
        r = requests.get('https://python666.cn/cls/number/guess/')
        num = int(r.text)
    except:                                                         #若网络异常则本地生成一个随机数
        num = random.randint(1,100)
    bingo = False
    while bingo == False:
        try:  # 验证输入的是否为数字
            answer = int(input("Guess a number between 1 to 100: "))
        except:
            print('Incorrect input. This round not accounted.')  # 输入错误不计入猜测轮数
            continue

        this_round += 1  # 确保输入正确后才计数
        if answer > num:
            print('Too big')
        elif answer < num:
            print('Too small')
        else:
            print('Bingo!')
            bingo = True
    return this_round


# 定义多次游戏，返回总游戏次数，最快猜中轮数，总游戏轮数
# 需要玩家名字，已有的总游戏次数，最快猜中轮数和总游戏轮数作为参数
def guess_all(name, game_times, min_round, total_round):
    if game_times > 0:
        ave_round = total_round / game_times
        print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
              % (name, game_times, min_round, ave_round))
    else:
        print('You are a new player. Welcome to the game.')

    play = 'Y'
    while play == 'Y':
        game_times += 1
        this_round = guess_one()    # 调用一次游戏的函数，
        total_round += this_round   # 把一次游戏的返回结果(本次游戏猜了几轮)加入到总游戏轮数中
        if min_round == 0 or this_round < min_round:  # 首次游戏或本次游戏猜对轮数小于之前最小轮数
            min_round = this_round
        print('%s, you played %d times, used %d round minimal to guess the answer, used %.2f rounds on average'
              % (name, game_times, min_round, total_round / game_times))

        play = input('Do you want to continue? Y to continue, others to quit.')
        if play != 'Y':
            return (game_times, min_round, total_round)


# 定义实现读取，游戏，存储全功能的函数
def main():
    name = input('Please enter your name: ')

    try:                                    #尝试打开文件
        with open('game.txt') as f:
            lines = f.readlines()
    except:                                 #若文件不存在则新建一个
        with open('game.txt','x') as f:
            lines = []                      #文件内容赋值为空列表防止之后出错

    scores = {}  # 新建一个空字典用来储存成绩
    for l in lines:
        record = l.split()  # 每一行的成绩按空格分隔并组成一个list
        scores[record[0]] = record[1:]  # 写入字典，名字作为key，成绩作为value

    if scores.get(name) == None:            #该用户在文件中不存在
        scores[name] = [0, 0, 0]
    game_times = int(scores[name][0])  # 总游戏次数
    min_round = int(scores[name][1])  # 最快猜中轮数
    total_round = int(scores[name][2])  # 总游戏轮数

    score = guess_all(name, game_times, min_round, total_round)     #调用多次游戏函数
    scores[name] = [str(score[0]), str(score[1]), str(score[2])]    #将多次函数的返回值tuple里的元素分别转换成字符串并更新对应名字的字典值

    result = ''  # 新建一个空字符串
    for i in scores:  # 遍历字典
        line = i + ' ' + ' '.join(scores[i]) + '\n'  # 将列表形式的value以join方法变成字符串并与key拼接
        result += line  # 将每一行的内容拼接成字符串

    with open('game.txt', 'w') as f:
        f.writelines(result)  # 将记录写入文件

#运行函数
main()