'''
描述
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。

如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。

如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。


如，输入： By?e 输出： Be?y

数据范围：输入的字符串长度满足 
1≤n≤1000 

输入描述：
输入字符串
输出描述：
输出字符串
'''

while True:
    try:
        s = input()  # 读取输入字符串
        a = ''  # 用于存储字符串中的字母

        # 提取字母
        for i in s:
            if i.isalpha():
                a += i

        # 对提取的字母进行排序，不区分大小写
        b = sorted(a, key=str.upper)
        index = 0  # 用于跟踪排序后字母的位置
        d = ''  # 用于存储最终结果字符串

        # 重新构造结果字符串
        for i in range(len(s)):
            if s[i].isalpha():
                d += b[index]
                index += 1
            else:
                d += s[i]
        
        # 输出结果字符串
        print(d)
    except:
        break  # 处理所有输入后退出
