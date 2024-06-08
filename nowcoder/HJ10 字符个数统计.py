'''
描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。

数据范围： 
1≤n≤500 
输入描述：
输入一行没有空格的字符串。

输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。
'''

def count_unique_characters(s):
    """
    计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )

    :param s: 输入的字符串
    :return: 不同字符的个数
    """
    unique_chars = set()
    
    for char in s:
        if 0 <= ord(char) <= 127 and char != '\n':  # 检查字符是否在 ASCII 范围内
            unique_chars.add(char)
    
    return len(unique_chars)

# 读取输入的字符串
import sys
input_string = sys.stdin.read().strip()

# 计算并输出不同字符的个数
output_count = count_unique_characters(input_string)
print(output_count)
