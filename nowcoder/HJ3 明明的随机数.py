'''
描述
明明生成了
𝑁
N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围： 
1≤n≤1000  ，输入的数字大小满足 1≤val≤500 
输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果
'''
import sys

# 使用sys.stdin读取所有输入
input_lines = sys.stdin.read().splitlines()

# 读取第一行，表示随机整数的个数N
N = int(input_lines[0])

# 创建一个集合用于存储唯一的随机整数
unique_numbers = set()

# 从第二行开始读取N个随机整数，并添加到集合中
for i in range(1, N + 1):
    number = int(input_lines[i])
    unique_numbers.add(number)

# 将集合中的元素转换为列表并排序
sorted_numbers = sorted(unique_numbers)

# 按顺序输出处理后的结果
for number in sorted_numbers:
    print(number)
