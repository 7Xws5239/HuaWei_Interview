'''
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串
'''

def split_and_pad_string(s):
    """
    将输入字符串按长度为8进行拆分，如果最后一部分长度不足8，则在后面补0。

    :param s: 输入字符串
    :return: 拆分后的字符串列表
    """
    result = []
    while len(s) > 8:
        result.append(s[:8])
        s = s[8:]
    
    # 处理最后一部分
    if len(s) > 0:
        result.append(s.ljust(8, '0'))
    
    return result

def process_input(strings):
    """
    处理输入字符串列表，按要求拆分每个字符串并输出结果。

    :param strings: 输入字符串列表
    """
    for s in strings:
        # 对每个字符串进行拆分和补0
        result = split_and_pad_string(s)
        for part in result:
            print(part)

# 读取连续输入的字符串（假设使用空行结束输入）
import sys
input_strings = []
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break
    input_strings.append(line)

# 处理输入字符串
process_input(input_strings)
