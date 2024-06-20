'''
计算一系列数的和
打开以下链接可以查看正确的代码
1
https://ac.nowcoder.com/acm/contest/5657#question

数据范围：数据组数满足 1≤t≤100  ，每组数据中整数个数满足 1≤n≤100  ，每组数据中的值满足 1≤val≤100 

输入描述：
输入数据包括多组。
每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
接下来n个正整数,即需要求和的每个正整数。

输出描述：
每组数据输出求和的结果
'''

# import sys
# sum=0
# for line in sys.stdin:
#     numbers = list(map(int,line.strip().split()))
#     n=numbers[0]
#     if n==0:
#         break
#     for i in range(1,len(numbers)):
#         sum=sum+numbers[i]

# print(sum)


import sys

sum = 0

# 读取第一行，确定后续数据行数
first_line = sys.stdin.readline().strip()
n = int(first_line)

# 如果第一行的数是0，则直接停止输入
if n == 0:
    print(sum)
    sys.exit()

# 读取后续的每一行数据并累加
for _ in range(n):
    line = sys.stdin.readline().strip()
    number = int(line)
    sum += number

print(sum)
