'''
描述
按照指定规则对输入的字符串进行处理。

详细描述：

第一步：将输入的两个字符串str1和str2进行前后合并。如给定字符串 "dec" 和字符串 "fab" ， 合并后生成的字符串为 "decfab"

第二步：对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标的意思是字符在字符串中的位置。注意排序后在新串中仍需要保持原来的奇偶性。例如刚刚得到的字符串“decfab”，分别对下标为偶数的字符'd'、'c'、'a'和下标为奇数的字符'e'、'f'、'b'进行排序（生成 'a'、'c'、'd' 和 'b' 、'e' 、'f'），再依次分别放回原串中的偶数位和奇数位，新字符串变为“abcedf”

第三步：对排序后的字符串中的'0'~'9'、'A'~'F'和'a'~'f'字符，需要进行转换操作。
转换规则如下：
对以上需要进行转换的字符所代表的十六进制用二进制表示并倒序，然后再转换成对应的十六进制大写字符（注：字符 a~f 的十六进制对应十进制的10~15，大写同理）。
如字符 '4'，其二进制为 0100 ，则翻转后为 0010 ，也就是 2 。转换后的字符为 '2'。
如字符 ‘7’，其二进制为 0111 ，则翻转后为 1110 ，对应的十进制是14，转换为十六进制的大写字母为 'E'。
如字符 'C'，代表的十进制是 12 ，其二进制为 1100 ，则翻转后为 0011，也就是3。转换后的字符是 '3'。
根据这个转换规则，由第二步生成的字符串 “abcedf” 转换后会生成字符串 "5D37BF"。


数据范围：输入的字符串长度满足  
1≤n≤100 

输入描述：
样例输入两个字符串，用空格隔开。

输出描述：
输出转化后的结果。
'''

def hex_reverse_transform(char):
    # 将字符转换为十六进制数值
    if char.isdigit():
        num = int(char)
    else:
        num = int(char, 16)
    
    # 将十六进制数值转换为二进制字符串并翻转
    bin_str = bin(num)[2:].zfill(4)  # 转换为4位的二进制字符串
    reversed_bin_str = bin_str[::-1]
    
    # 将翻转后的二进制字符串转换回十六进制数值
    reversed_num = int(reversed_bin_str, 2)
    
    # 将数值转换回十六进制字符
    if reversed_num < 10:
        return str(reversed_num)
    else:
        return chr(reversed_num - 10 + ord('A'))

def process_strings(str1, str2):
    # 第一步：合并字符串
    combined_str = str1 + str2
    
    # 第二步：分别对奇数和偶数下标的字符进行排序
    even_chars = sorted(combined_str[0::2])
    odd_chars = sorted(combined_str[1::2])
    
    sorted_combined_str = []
    even_index = odd_index = 0
    
    for i in range(len(combined_str)):
        if i % 2 == 0:
            sorted_combined_str.append(even_chars[even_index])
            even_index += 1
        else:
            sorted_combined_str.append(odd_chars[odd_index])
            odd_index += 1
    
    sorted_combined_str = ''.join(sorted_combined_str)
    
    # 第三步：对特定字符进行十六进制转换
    transformed_str = []
    for char in sorted_combined_str:
        if char.isdigit() or ('A' <= char <= 'F') or ('a' <= char <= 'f'):
            transformed_str.append(hex_reverse_transform(char))
        else:
            transformed_str.append(char)
    
    return ''.join(transformed_str)

# 读取输入
import sys
input_data = sys.stdin.read().strip().split()

# 假设输入为两部分，用空格隔开
str1 = input_data[0]
str2 = input_data[1]

# 处理字符串并输出结果
result = process_strings(str1, str2)
print(result)
