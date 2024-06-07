'''
描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。

数据范围：保证输入的数字在 32 位浮点数范围内
输入描述：
输入一个正浮点数值

输出描述：
输出该数值的近似整数值
'''

def approximate_integer(value):
    """
    根据四舍五入规则，返回一个浮点数的近似整数值。
    如果小数部分大于等于0.5，向上取整；小于0.5，向下取整。
    
    :param value: 输入的正浮点数
    :return: 近似整数值
    """
    # 使用内置函数math模块的floor和ceil来实现
    import math
    if value - math.floor(value) >= 0.5:
        return math.ceil(value)
    else:
        return math.floor(value)

def process_input(value):
    """
    处理输入的浮点数，输出其近似整数值。

    :param value: 输入的正浮点数
    """
    approx_value = approximate_integer(value)
    print(approx_value)

# 读取输入的浮点数
import sys
input_value = float(sys.stdin.read().strip())

# 处理输入的浮点数
process_input(input_value)
