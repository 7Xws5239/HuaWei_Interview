'''
计算a+b
打开以下链接可以查看正确的代码
1
https://ac.nowcoder.com/acm/contest/5657#question

数据范围：数据组数满足 1≤t≤100  ， 数据大小满足 1≤n≤100 

输入描述：
输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入

输出描述：
输出a+b的结果
'''

import sys

result = []
stn = sys.stdin
for line in stn:
    a, b = map(int, line.strip().split())
    if a == 0 and b == 0:
        break
    result.append(a + b)

for res in result:
    print(res)

