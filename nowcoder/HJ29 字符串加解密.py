'''
描述
对输入的字符串进行加解密，并输出。

加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

解密方法为加密的逆过程。
数据范围：输入的两个字符串长度满足 
1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成

输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码

输出描述：
第一行输出加密后的字符
第二行输出解密后的字符
'''

def encrypt(input_string):
    encrypted_string = []
    for char in input_string:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    encrypted_string.append('A')
                else:
                    encrypted_string.append(chr(ord(char) + 1).upper())
            elif char.isupper():
                if char == 'Z':
                    encrypted_string.append('a')
                else:
                    encrypted_string.append(chr(ord(char) + 1).lower())
        elif char.isdigit():
            if char == '9':
                encrypted_string.append('0')
            else:
                encrypted_string.append(str(int(char) + 1))
        else:
            encrypted_string.append(char)
    return ''.join(encrypted_string)

def decrypt(encrypted_string):
    decrypted_string = []
    for char in encrypted_string:
        if char.isalpha():
            if char.islower():
                if char == 'a':
                    decrypted_string.append('Z')
                else:
                    decrypted_string.append(chr(ord(char) - 1).upper())
            elif char.isupper():
                if char == 'A':
                    decrypted_string.append('z')
                else:
                    decrypted_string.append(chr(ord(char) - 1).lower())
        elif char.isdigit():
            if char == '0':
                decrypted_string.append('9')
            else:
                decrypted_string.append(str(int(char) - 1))
        else:
            decrypted_string.append(char)
    return ''.join(decrypted_string)

# 读取输入
import sys
input_data = sys.stdin.read().strip().split()
original_string = input_data[0]
encrypted_string = input_data[1]

# 加密并输出结果
print(encrypt(original_string))

# 解密并输出结果
print(decrypt(encrypted_string))
