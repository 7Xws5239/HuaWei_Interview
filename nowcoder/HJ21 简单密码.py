'''
描述
现在有一种密码变换算法。
九键手机键盘上的数字与字母的对应： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，把密码中出现的小写字母都变成九键键盘对应的数字，如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
数字和其它的符号都不做变换。
数据范围： 输入的字符串长度满足 1≤n≤100 
输入描述：
输入一组密码，长度不超过100个字符。

输出描述：
输出密码变换后的字符串
'''

def transform_password(password):
    """
    根据描述的密码变换规则转换密码
    :param password: 输入的密码字符串
    :return: 变换后的密码字符串
    """
    # 定义九键键盘上数字与字母的对应关系
    keyboard_mapping = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }
    
    result = []
    
    for char in password:
        if char.islower():
            # 小写字母变为九键键盘对应的数字
            result.append(keyboard_mapping[char])
        elif char.isupper():
            # 大写字母变为小写并往后移一位
            lower_char = char.lower()
            if lower_char == 'z':
                result.append('a')
            else:
                result.append(chr(ord(lower_char) + 1))
        else:
            # 数字和其他符号不变
            result.append(char)
    
    return ''.join(result)

# 读取输入
if __name__ == "__main__":
    import sys
    input_password = sys.stdin.read().strip()
    # 进行密码变换
    output_password = transform_password(input_password)
    # 输出结果
    print(output_password)
