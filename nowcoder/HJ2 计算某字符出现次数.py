'''
描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围： 
1≤n≤1000 
输入描述：
第一行输入一个由字母、数字和空格组成的字符串，第二行输入一个字符（保证该字符不为空格）。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）
'''

import sys

# 使用sys.stdin.read().splitlines()读取所有输入行并分割成列表
input_lines = sys.stdin.read().splitlines()

# 获取第一行输入，即字符串
input_string = input_lines[0]
# 获取第二行输入，即要查找的字符
search_char = input_lines[1]

# 将字符串和字符都转换为小写，以实现不区分大小写的比较
input_string_lower = input_string.lower()
search_char_lower = search_char.lower()


# 计算字符串中指定字符的出现次数
count = input_string_lower.count(search_char_lower)

# 输出结果
print(count)
