'''
描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。


数据范围： 

1≤n≤100  ，输入的数据大小满足 
2≤val≤30000 

输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。
'''

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(nums):
    n = len(nums)
    # 初始化图，两个部分：一个部分存储奇数，另一个部分存储偶数
    odd_nums = [x for x in nums if x % 2 != 0]
    even_nums = [x for x in nums if x % 2 == 0]
    
    # 构建二分图
    matches = {}
    for odd in odd_nums:
        matches[odd] = []
        for even in even_nums:
            if is_prime(odd + even):
                matches[odd].append(even)

    # 匈牙利算法实现二分图最大匹配
    def bpm(u, seen, match):
        for v in matches[u]:
            if not seen[v]:
                seen[v] = True
                if v not in match or bpm(match[v], seen, match):
                    match[v] = u
                    return True
        return False

    match = {}
    result = 0
    for u in odd_nums:
        seen = {v: False for v in even_nums}
        if bpm(u, seen, match):
            result += 1

    return result

# 读取输入
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
nums = list(map(int, data[1:n + 1]))

# 计算结果并输出
result = find_prime_pairs(nums)
print(result)
