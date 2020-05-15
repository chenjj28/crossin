# 56.生兔子问题
# 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问第10个月的兔子总数为多少？

# Method1 - 斐波那契数列
lst = [2,2]
for i in range (2,10):
    lst.append(lst[i-2]+lst[i-1])
print(lst)


# Method2 - 面向对象
class Rab:
    def __init__(self):
        self.age = 0

    def grow(self):
        self.age += 1

    def breed(self):
        if self.age > 2:        #如果年龄大于两个月就会繁殖
            return Rab()

a = Rab()
family = [a]
month = 10
for i in range(month):
    for member in family:
        member.grow()           #每一对兔子长大一个月
        child = member.breed()  #每一对符合条件的兔子都繁殖
        if child:               #如果繁殖成功
            lst.append(child)   #加入到family列表

print(len(lst)*2)


# 57.输出素数
# 判断101-200之间有多少个素数，并输出所有素数。
count = 0
for i in range(101,200):
    for j in range (2,i-1):
        if i%j == 0:
            break
    else:
        print(i)
        count += 1
print('There are total %d numbers.' %count)


# 58.水仙花数
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100,1000):
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    if i == pow(a,3) + pow(b,3) + pow(c,3):
        print(i)

#参考答案
for n in range(100,1000):
    i = n // 100                百位
    j = n // 10 % 10            十位
    k = n % 10                  个位
    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)
# //是取整除 - 返回商的整数部分（向下取整）


# 59.完数
# 一个数如果恰好等于它的因子（即除了自身以外的约数）之和，
# 这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
for i in range(5, 10):
    divisor = []
    for j in range(1,i):
        if i%j == 0:
            divisor.append(j)
    if i == sum(divisor):
        print(i, divisor)


# 60.自由落下的球
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height = 100
count = 0
for n in range(1,11):
    count += height     #第n次落地前
    height = height/2   #落地后反弹高度
    count += height     #经过长度加反弹高度

print('第10次落地时共经过',count-height)
print('第10次反弹',height)
