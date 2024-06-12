'''
计算a+b
打开以下链接可以查看正确的代码
https://ac.nowcoder.com/acm/contest/5657#question

数据范围： 数据组数 1≤t≤100  , 数据大小满足 1≤n≤1000 


输入描述：
输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。

输出描述：
输出a+b的结果
'''

import sys

data = sys.stdin.read().strip().split('\n')
result = []
for item in data:
    a,b = map(int,item.split())
    result.append(a+b)

print(result)



# import sys

# data = sys.stdin.read().strip().split('\n')

# print(data)

# result = []

# def doubler(s) -> int:
#     return int(s) * 2

# for item in data:
#     a,b = map(doubler, item.split()) #对每一个元素都执行doubler
#     result.append(a+b)

# print(result)

