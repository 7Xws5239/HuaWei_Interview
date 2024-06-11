'''
描述
N 位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。

设K位同学从左到右依次编号为 1，2…，K ，他们的身高分别为T1,T2,…,TK，若存在`(1≤i≤K) 使得T1<T2<......<Ti−1<Ti且 Ti>Ti+1>......>TK，
则称这K名同学排成了合唱队形。
通俗来说，能找到一个同学，他的两边的同学身高都依次严格降低的队形就是合唱队形。
例子：
123 124 125 123 121 是一个合唱队形
123 123 124 122不是合唱队形，因为前两名同学身高相等，不符合要求
123 122 121 122不是合唱队形，因为找不到一个同学，他的两侧同学身高递减。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等

数据范围：  1≤n≤3000 

输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列
'''

import bisect

def inc_max(l):
    """
    计算每个位置的最长递增子序列长度（LIS）。
    
    :param l: 输入的高度列表
    :return: 每个位置的LIS长度
    """
    dp = [1] * len(l)  # 初始化dp数组，每个位置的最小递增子序列长度为1
    arr = [l[0]]  # 创建数组存储当前的LIS
    for i in range(1, len(l)):  # 从第二个元素开始遍历
        if l[i] > arr[-1]:
            arr.append(l[i])
            dp[i] = len(arr)  # 更新dp数组当前位置的LIS长度
        else:
            pos = bisect.bisect_left(arr, l[i])  # 找到arr中第一个不小于l[i]的位置
            arr[pos] = l[i]  # 用l[i]替换arr中这个位置的元素
            dp[i] = pos + 1  # 更新dp数组当前位置的LIS长度
    return dp

while True:
    try:
        N = int(input())  # 读取同学总数
        s = list(map(int, input().split()))  # 读取同学的身高列表
        left_s = inc_max(s)  # 计算从左到右的LIS长度
        right_s = inc_max(s[::-1])[::-1]  # 计算从右到左的LIS长度，并反转回来
        sum_s = [left_s[i] + right_s[i] - 1 for i in range(len(s))]  # 计算每个位置的合唱队形长度，并减去重复计算的最高点
        print(str(N - max(sum_s)))  # 计算并输出最少需要出列的同学数量
    except:
        break  # 处理所有输入后退出
