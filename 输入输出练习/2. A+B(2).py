'''
计算a+b
打开以下链接可以查看正确的代码
1
https://ac.nowcoder.com/acm/contest/5657#question

数据范围：数据组数满足 1≤t≤100  ，数据大小满足 1≤a,b≤1000 


输入描述：
输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 1000)

输出描述：
输出a+b的结果
'''

import sys

data = sys.stdin.read().strip().split('\n')

d_len = len(data)
result = []
for i in range(1,d_len):
    a,b=map(int,data[i].strip().split())
    result.append(a+b)

print(result)