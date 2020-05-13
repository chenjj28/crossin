# 46.计算列表元素之积
# 定义一个数字列表 [2,4,1,2]，并计算列表元素之积。
num_list = [2,4,1,2]
mul = 1
for i in num_list:
    mul *= i
print(mul)


# 47.计算数字列表被最大数与最小数之差
# 定义一个数字列表 [2,4,1,2]，并计算列表元素最大数与最小数之差。
lst = [2,4,1,2]
lst.sort()
diff = lst[-1]-lst[0]
print(diff)

# or
print(max(lst)-min(lst))


# 48.最大公约数算法
# 任意输入两个整数求他们的最大公约数
a = int(input('Please enter 1st number: '))
b = int(input('Please enter 2nd number: '))
smaller = min(a,b)
for i in range(1,smaller+1):
    if a%i == 0 and b%i == 0:
        gcd = i
print(gcd)


# 49.最小公倍数算法
a = int(input('Please enter 1st number: '))
b = int(input('Please enter 2nd number: '))
bigger = max(a,b)
smaller = min(a,b)
for i in range(1,smaller+1):
    if bigger*i%smaller == 0:
        lcm = i*bigger
        break
print(lcm)


# 50.字符串翻转
# 给定一个字符串如 "Crossin的编程教室"，然后将其翻转，逆序输出
string = 'Crossin的编程教室'
lst = list(string)
lst.reverse()
r_string = ''.join(lst)
print(r_string)

# or
print(string[::-1])