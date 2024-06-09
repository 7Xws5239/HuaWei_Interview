'''
描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址从1.0.0.0到126.255.255.255;

B类地址从128.0.0.0到191.255.255.255;

C类地址从192.0.0.0到223.255.255.255;

D类地址从224.0.0.0到239.255.255.255；

E类地址从240.0.0.0到255.255.255.255


私网IP范围是：

从10.0.0.0到10.255.255.255

从172.16.0.0到172.31.255.255

从192.168.0.0到192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
（注意二进制下全是1或者全是0均为非法子网掩码）

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。

请参考帖子https://www.nowcoder.com/discuss/276处理循环输入的问题。
输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''

ipClass2num = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'ERROR': 0,
    'PRIVATE': 0,
}

def check_ip(ip: str) -> bool:
    """
    检查IP地址是否合法
    :param ip: 输入的IP地址
    :return: 合法返回True，否则返回False
    """
    ip_bit = ip.split('.')
    if len(ip_bit) != 4 or '' in ip_bit:  # IP的长度应为4且每一位不为空
        return False
    for i in ip_bit:
        if int(i) < 0 or int(i) > 255:  # 检查IP每一部分的值范围应为0~255
            return False
    return True

def check_mask(mask: str) -> bool:
    """
    检查子网掩码是否合法
    :param mask: 输入的子网掩码
    :return: 合法返回True，否则返回False
    """
    if not check_ip(mask):
        return False
    if mask == '255.255.255.255' or mask == '0.0.0.0':
        return False
    mask_list = mask.split('.')
    if len(mask_list) != 4:
        return False
    mask_bit = []
    for i in mask_list:  # 将每个掩码段转换为二进制字符串
        i = bin(int(i))  # 转换为二进制
        i = i[2:]  # 去掉前缀'0b'
        mask_bit.append(i.zfill(8))  # 每段二进制填充到8位
    whole_mask = ''.join(mask_bit)  # 拼接成完整的二进制掩码字符串
    whole0_find = whole_mask.find("0")  # 找到第一个'0'的位置
    whole1_rfind = whole_mask.rfind("1")  # 找到最后一个'1'的位置
    if whole1_rfind + 1 == whole0_find:  # 掩码格式合法要求最后一个'1'后面全是'0'
        return True
    else:
        return False

def check_private_ip(ip: str) -> bool:
    """
    检查IP地址是否为私有IP
    :param ip: 输入的IP地址
    :return: 是私有IP返回True，否则返回False
    """
    ip_list = ip.split('.')
    if ip_list[0] == '10':
        return True
    if ip_list[0] == '172' and 16 <= int(ip_list[1]) <= 31:
        return True
    if ip_list[0] == '192' and ip_list[1] == '168':
        return True
    return False

while True:
    try:
        s = input()
        ip = s.split('~')[0]
        mask = s.split('~')[1]
        if check_ip(ip):
            first = int(ip.split('.')[0])
            if first == 127 or first == 0:
                # 忽略0.*.*.*和127.*.*.*类型的IP地址
                continue
            if check_mask(mask):
                if check_private_ip(ip):
                    ipClass2num['PRIVATE'] += 1
                if 0 < first < 127:
                    ipClass2num['A'] += 1
                elif 127 < first <= 191:
                    ipClass2num['B'] += 1
                elif 192 <= first <= 223:
                    ipClass2num['C'] += 1
                elif 224 <= first <= 239:
                    ipClass2num['D'] += 1
                elif 240 <= first <= 255:
                    ipClass2num['E'] += 1
            else:
                ipClass2num['ERROR'] += 1
        else:
            ipClass2num['ERROR'] += 1
    except:
        break

# 输出结果
for v in ipClass2num.values():
    print(v, end=' ')
