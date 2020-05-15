# 给定一个屏蔽词列表的文件，文件中每一行都是一个词汇，可能是英文也可能是中文。
# 实现一个方法，输入一段文字，将其中存在于列表中的词汇字符替换成 *，返回处理后的文字。

text = input('Please enter the sentense: ')
with open('block.txt') as f:
    block = f.readlines()
for word in block:
    w = word.strip('\n')
    if w in text:
        text = text.replace(w, '*'*len(w))
print(text)
