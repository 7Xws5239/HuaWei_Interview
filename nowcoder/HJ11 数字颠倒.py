'''
描述
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001


数据范围： 
0≤n≤2的30−1 

输入描述：
输入一个int整数

输出描述：
将这个整数以字符串的形式逆序输出
'''

def reverse_integer(n):
    """
    将输入的整数以字符串形式逆序输出。

    :param n: 输入的整数
    :return: 逆序后的字符串
    """
    # 将整数转换为字符串
    str_n = str(n)
    # 将字符串逆序
    reversed_str_n = str_n[::-1]
    return reversed_str_n

# 读取输入的整数
import sys
input_number = int(sys.stdin.read().strip())

# 处理输入的整数并输出结果
output_string = reverse_integer(input_number)
print(output_string)
