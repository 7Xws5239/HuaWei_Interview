'''
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围： 
1≤n≤10的8
  
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
'''

def reverse_and_remove_duplicates(n):
    """
    按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

    :param n: 输入的int型整数
    :return: 不含重复数字的新整数
    """
    seen = set()
    result = []

    # 将整数转换为字符串，从右向左遍历
    for digit in reversed(str(n)):
        if digit not in seen:
            seen.add(digit)
            result.append(digit)
    
    # 将结果列表转换为字符串，再转换为整数
    return int("".join(result))

# 读取输入的整数
import sys
input_number = int(sys.stdin.read().strip())

# 处理输入的整数并输出结果
output_number = reverse_and_remove_duplicates(input_number)
print(output_number)
