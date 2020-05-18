# 61.猴子吃桃问题
# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，又多吃了一个，
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
a = 1
for i in range (9):
    a = (a+1)*2
    print('Day %d have %d' %(9-i, a))


# 62.乒乓球比赛
# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
import itertools
team1 = ['a','b','c']                           #看做abc顺序不变
team2 = list(itertools.permutations('xyz',3))   #xyz不放回抽样排列得到一个由tuple组成的list

for i in team2:
    if i[0] != 'x' and i[2] !='x' and i[2] !='z':
        for n in range(3):
            print('%s vs %s' %(team1[n], i[n]))


# 63.打印菱形图案
for i in range(1,5):
    print((4-i)*' ' + (2*i-1)*'*')
for i in range(1,4):
    print(i*' ' + (7-2*i)*'*')


# 64.求分数序列之和
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
a = 2
b = 1
lst = [a/b]
for i in range(19):
    a = a+b
    b = a-b
    lst.append(a/b)
print(sum(lst))


# 65.求阶乘数之和
# 求1+2!+3!+...+20!的和。n!=1×2×3×...×n
m = 0
for i in range (1,21):
    n = 1
    for j in range(1,i+1):
        n *= j
    m += n
print(m)

# 参考答案
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print(s)