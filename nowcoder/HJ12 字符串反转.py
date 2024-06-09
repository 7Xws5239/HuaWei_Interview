'''
描述
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

输入描述：
输入一行，为一个只包含小写字母的字符串。

输出描述：
输出该字符串反转后的字符串。
'''

def reverse_string(s):
    """
    将输入的字符串反转后输出。

    :param s: 输入的字符串
    :return: 反转后的字符串
    """
    # 使用字符串切片操作将字符串逆序
    reversed_str = s[::-1]
    return reversed_str

# 读取输入的字符串
import sys
input_string = sys.stdin.read().strip()

# 处理输入的字符串并输出结果
output_string = reverse_string(input_string)
print(output_string)
