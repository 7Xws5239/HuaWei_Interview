'''
描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 x ，让你寻找 x 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。

数据范围：

1≤n≤1000 ，输入的字符串长度满足 1≤len(str)≤10  ， 1≤k<n 

输入描述：
输入只有一行。 先输入字典中单词的个数n，再输入n个单词作为字典单词。 然后输入一个单词x 最后后输入一个整数k

输出描述：
第一行输出查找到x的兄弟单词的个数m 第二行输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。
'''

def find_brother_words(n, words, x, k):
    # 过滤出所有兄弟单词
    brother_words = [word for word in words if sorted(word) == sorted(x) and word != x]

    # 按字典序排序
    brother_words.sort()

    # 输出兄弟单词的数量
    print(len(brother_words))
    
    # 输出第 k 个兄弟单词（如果存在）
    if k <= len(brother_words):
        print(brother_words[k - 1])

# 读取输入
input_data = input().strip().split()
n = int(input_data[0])
words = input_data[1:n + 1]
x = input_data[n + 1]
k = int(input_data[n + 2])

# 查找并输出结果
find_brother_words(n, words, x, k)
