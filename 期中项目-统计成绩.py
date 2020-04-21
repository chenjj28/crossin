# 读取 report.txt 文件中的成绩；
# 统计每名学生总成绩、计算平均并从高到低重新排名；
# 汇总每一科目的平均分和总平均分（见下表第一行）；
# 添加名次，替换60分以下的成绩为“不及格”；
# 将处理后的成绩另存为一个新文件（result.txt）。

with open ('report.txt') as f:
    lines = f.readlines()

std_list = []
for line in lines:
    line = line.split()                  #每个学生单独一个列表
    std_list.append(line)               #所有学生的成绩汇总成一个嵌套列表
std_list[0].insert(0,'名次')
std_list[0].append('总分')
std_list[0].append('平均分')
# print(std_list)

#计算每个学生的总分和平均分
for std in std_list[1:]:                        #遍历除标题行外每个学生的成绩列表
    total = sum(int(x) for x in std[1:])        #计算每个学生的总分
    average = '%.1f' %(total/9)                 #计算每个学生的平均分
    std.append('%d' %total)                     #每个学生的列表中增加总分
    std.append(average)                         #每个学生的列表中增加平均分
# print(std_list)

sortlist = sorted(std_list[1:], key=lambda x: int(x[-2]), reverse=True)        #通过总成绩排序
# print(sortlist)

#计算没门课的平均分并替换60分以下的成绩
ave_list = []                                           #每门课的平均分列表
for i in range(1,12):
    sub_sum = 0
    for j in range(len(sortlist)):
        sub_sum += float(sortlist[j][i])
        if float(sortlist[j][i]) < 60.0 and i < 10:     #替换60分以下的成绩（不包括总分和平均分）
            sortlist[j][i] = "不及格"
    sub_ave = '%.1f' %(sub_sum/(len(sortlist)))
    ave_list.append(sub_ave)
ave_list.insert(0,'平均')
sortlist.insert(0,ave_list)
# print(sortlist)

#增加排名
for n in range(len(sortlist)):
    sortlist[n].insert(0,'%d' %n)                       #str类型，方便之后合并列表
# print(sortlist)

sortlist.insert(0,std_list[0])                          #将标题行插入已经排序过的成绩嵌套列表

with open('result.txt','w') as f:
    for i in sortlist:
        result = '  '.join(i)
        f.writelines(result + '\n')
