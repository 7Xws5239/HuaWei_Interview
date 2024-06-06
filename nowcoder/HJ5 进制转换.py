'''
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 
1≤n≤2的31−1 
输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
'''

def hex_to_decimal(hex_string):
    """
    将十六进制字符串转换为十进制整数。

    :param hex_string: 输入的十六进制字符串
    :return: 对应的十进制整数的字符串表示
    """
    # 使用int函数将十六进制字符串转换为十进制整数
    return str(int(hex_string, 16))

def process_input(hex_strings):
    """
    处理输入的十六进制字符串列表，转换为十进制并输出结果。

    :param hex_strings: 输入的十六进制字符串列表
    """
    results = []
    for hex_string in hex_strings:
        # 对每个十六进制字符串进行转换
        decimal_string = hex_to_decimal(hex_string)
        results.append(decimal_string)
    
    # 使用\n连接结果字符串，符合输出描述
    output = "\n".join(results)
    print(output)

# 读取连续输入的十六进制字符串（假设使用空行结束输入）
import sys
input_hex_strings = []
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    input_hex_strings.append(line)

# 处理输入字符串
process_input(input_hex_strings)
