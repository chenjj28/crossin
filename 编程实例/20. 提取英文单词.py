# from .txt 是一个混杂了英文单词和中文的文本文件。
# 要求：把from .txt 里的文件复制到to.txt里，但只复制其中的英文单词，并按字母序排序。
import re
with open('from.txt') as f:
    text = f.read()

new = re.findall(r"\b[A-z]+\b", text)
new.sort()

with open('to.txt','w') as f:
    for i in new:
        f.writelines(i + '\n')
