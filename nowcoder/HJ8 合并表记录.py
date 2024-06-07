'''
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。


提示:
0 <= index <= 11111111
1 <= value <= 100000

输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）
'''

def merge_records(n, records):
    """
    合并相同索引的记录，并按索引值升序输出结果。

    :param n: 键值对的个数
    :param records: 包含索引和值的记录列表
    :return: 合并后的记录字典
    """
    from collections import defaultdict

    # 使用defaultdict来存储合并结果
    merged_records = defaultdict(int)
    
    for index, value in records:
        merged_records[index] += value
    
    # 按照索引值升序排序并输出
    for index in sorted(merged_records.keys()):
        print(index, merged_records[index])

# 读取输入
import sys
input_data = sys.stdin.read().strip().split()
n = int(input_data[0])

records = []
for i in range(1, len(input_data), 2):
    index = int(input_data[i])
    value = int(input_data[i + 1])
    records.append((index, value))

# 处理并输出合并结果
merge_records(n, records)
