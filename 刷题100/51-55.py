# 51.输入十进制数转二进制、八进制、十六进制
a = int(input('输入要转换的十进制数字: '))
print('二进制:', bin(a))
print('八进制:', oct(a))
print('十六进制:', hex(a))


# 52.信息加密
# 某个公司采用公用电话传递数据，数据是四位的整数，如2126 ，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，2126：(2+5)%10; (1+5)%10; (2+5)%10;(6+5)%10
# 再将第一位和第四位交换，第二位和第三位交换。

# Method 1
msg = input('Please enter the 4-dig number: ')
lst = list(msg)                 #此时列表中每个元素都是字符串形式
pw = list(map(lambda x: (int(x)+5)%10, lst))    #map函数作用于列表中每个元素
pw.reverse()
for i in pw:
    print(i,end='')

# Method 2
msg = input('Please enter the 4-dig number: ')
pw = [str((int(i)+5)%10) for i in msg]
print(''.join(pw[::-1]))


# 53.第n个斐波那契数
# 指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
# 斐波那契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
n = int(input('Please enter the number: '))
lst = [1,1]
for i in range(2, n):
    lst.append(lst[i-1] + lst[i-2])
print(lst)


# 54.奖金提成
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
i = int(input('Please enter the profit: '))
profit = [10,20,40,60,100]
ratio = [0.1,0.075,0.05,0.03,0.01]
bonous = 0
for n in range(5):
    if i > profit[n]:
        bonous += profit[n] * ratio[n]
    else:
        bonous += (i-profit[n-1]) * ratio[n]
        break
print(bonous)


# 55.数字组合问题
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print(str(i)+str(j)+str(k))
                count +=1
print('There are total %d numbers.' %count)