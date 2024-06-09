'''
描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1≤n≤100 
输入描述：
一组字符串。

输出描述：
如果符合要求输出：OK，否则输出NG
'''

import re

def check_length(password):
    """
    检查密码长度是否超过8位
    """
    return len(password) > 8

def check_char_types(password):
    """
    检查密码是否包含至少三种字符类型（大写字母、小写字母、数字、其他符号）
    """
    count = 0
    if re.search(r'[A-Z]', password):
        count += 1
    if re.search(r'[a-z]', password):
        count += 1
    if re.search(r'[0-9]', password):
        count += 1
    if re.search(r'[^A-Za-z0-9]', password):
        count += 1
    return count >= 3

def check_repeated_substring(password):
    """
    检查密码中是否包含长度大于2的重复子串
    """
    length = len(password)
    for i in range(length - 2):
        for j in range(i + 3, length - 2 + i + 3):
            if j <= length:
                if password[i:i+3] in password[j:]:
                    return False
    return True

def check_password(password):
    """
    检查密码是否符合所有要求
    """
    if check_length(password) and check_char_types(password) and check_repeated_substring(password):
        return "OK"
    else:
        return "NG"

if __name__ == "__main__":
    import sys
    passwords = sys.stdin.read().strip().split()
    for password in passwords:
        print(check_password(password))
