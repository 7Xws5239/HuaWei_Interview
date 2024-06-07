'''
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）


数据范围： 
1≤n≤2×10的9+14 
输入描述：
输入一个整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
'''

def prime_factors(n):
    """
    返回一个整数 n 的所有质因子，按照从小到大的顺序排列。

    :param n: 输入的正整数
    :return: 质因子列表
    """
    factors = []
    
    # 处理2的因子
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # 处理其他质因子
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    # 如果 n 是一个大于 2 的质数
    if n > 2:
        factors.append(n)
    
    return factors

def process_input(number):
    """
    处理输入的数字，输出它的所有质因子。

    :param number: 输入的正整数
    """
    factors = prime_factors(number)
    # 将因子列表转换为字符串，并用空格连接
    output = " ".join(map(str, factors))
    print(output)

# 读取输入的整数
import sys
input_number = int(sys.stdin.read().strip())

# 处理输入的整数
process_input(input_number)
