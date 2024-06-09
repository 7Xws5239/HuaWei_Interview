'''
描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

数据范围：保证在 32 位整型数字范围内
输入描述：
 输入一个整数（int类型）

输出描述：
 这个数转换成2进制后，输出1的个数
'''

def count_ones(n):
    """
    计算整数 n 的二进制表示中 1 的个数。

    :param n: 输入的整数
    :return: 二进制表示中 1 的个数
    """
    # 使用 bin 函数将整数转换为二进制字符串，并计算 '1' 的个数
    return bin(n).count('1')

# 读取输入的整数
import sys
input_number = int(sys.stdin.read().strip())

# 计算并输出二进制表示中 1 的个数
output_count = count_ones(input_number)
print(output_count)
