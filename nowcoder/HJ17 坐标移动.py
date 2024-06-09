'''
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足 1≤n≤10000  ，坐标保证满足 −2的31≤x,y≤2的31−1  ，且数字部分仅含正数
输入描述：
一行字符串

输出描述：
最终坐标，以逗号分隔
'''

def is_valid_coordinate(coordinate):
    """
    判断一个坐标字符串是否有效。
    有效的坐标为 A/D/W/S 后跟 1 或 2 位数字。
    
    :param coordinate: 输入的坐标字符串
    :return: 如果坐标有效返回 True，否则返回 False
    """
    if len(coordinate) < 2 or len(coordinate) > 3:
        return False
    if coordinate[0] not in 'ADWS':
        return False
    if not coordinate[1:].isdigit():
        return False
    return True

def calculate_final_position(commands):
    """
    计算最终的坐标位置。

    :param commands: 输入的移动命令字符串，以 ';' 分隔
    :return: 最终的坐标位置
    """
    x, y = 0, 0
    for command in commands.split(';'):
        if is_valid_coordinate(command):
            direction = command[0]
            value = int(command[1:])
            if direction == 'A':
                x -= value
            elif direction == 'D':
                x += value
            elif direction == 'W':
                y += value
            elif direction == 'S':
                y -= value
    return x, y

# 读取输入
import sys
input_string = sys.stdin.read().strip()

# 计算最终坐标
final_x, final_y = calculate_final_position(input_string)

# 输出结果
print(f"{final_x},{final_y}")
