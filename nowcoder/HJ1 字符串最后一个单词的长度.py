'''
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。
'''

import sys

# 通过sys.stdin读取输入行
for line in sys.stdin:
    # 使用split方法将字符串按空格分割成单词列表
    words = line.split()
    # 获取最后一个单词
    last_word = words[-1]
    # 输出最后一个单词的长度
    print(len(last_word))
