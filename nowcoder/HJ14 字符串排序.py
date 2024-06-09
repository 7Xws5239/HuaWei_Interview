'''
描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。

数据范围： 
1≤n≤1000  ，字符串长度满足 1≤len≤100 

输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。

输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
'''

def sort_strings(n, strings):
    """
    对n个字符串按照字典序进行排序。

    :param n: 字符串的个数
    :param strings: 字符串列表
    :return: 排序后的字符串列表
    """
    # 按照字典序对字符串列表进行排序
    sorted_strings = sorted(strings)
    return sorted_strings

# 读取输入
import sys
input_data = sys.stdin.read().strip().split('\n')

# 第一个输入为字符串个数
n = int(input_data[0])

# 读取接下来的n个字符串
strings = input_data[1:n+1]

# 对字符串进行排序
sorted_strings = sort_strings(n, strings)

# 输出排序后的字符串
for string in sorted_strings:
    print(string)
