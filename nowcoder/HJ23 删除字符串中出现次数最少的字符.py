'''
描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足 1≤n≤20  ，保证输入的字符串中仅出现小写字母
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述：
删除字符串中出现次数最少的字符后的字符串。
'''

def remove_least_frequent_chars(s):
    # 计算每个字符出现的次数
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 找到最少出现次数
    min_count = min(char_count.values())
    
    # 构建新的字符串，排除出现次数最少的字符
    result = ''.join([char for char in s if char_count[char] != min_count])
    
    return result

# 读取输入
input_str = input().strip()

# 处理字符串并输出结果
output_str = remove_least_frequent_chars(input_str)
print(output_str)
