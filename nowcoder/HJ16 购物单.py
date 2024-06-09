'''
描述
王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。
每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。
王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 ~ 5 表示。
他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。
满意度是指所购买的每件物品的价格与重要度的乘积的总和，
假设设第i件物品的价格为v[i]，重要度为w[i]，共选中了k件物品，编号依次为j1,j2,...,jk，则满意度为：v[j1]∗w[j1]+v[j2]∗w[j2]+…+v[jk]∗w[jk]。（其中 * 为乘号）
请你帮助王强计算可获得的最大的满意度。


输入描述：
输入的第 1 行，为两个正整数N，m，用一个空格隔开：

（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）


从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q


（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
 



输出描述：
 输出一个正整数，为张强可以获得的最大的满意度。
'''

def maximize_satisfaction(N, m, items):
    """
    计算在预算N元内可以获得的最大满意度。

    :param N: 总预算
    :param m: 物品的数量
    :param items: 物品列表，每个元素是一个包含(v, p, q)的元组
    :return: 最大满意度
    """
    from collections import defaultdict

    # 将物品分为主件和附件
    main_items = []
    attach_items = defaultdict(list)
    
    for i in range(m):
        v, p, q = items[i]
        if q == 0:
            main_items.append((i + 1, v, p))  # (编号, 价格, 重要度)
        else:
            attach_items[q].append((i + 1, v, p))  # (编号, 价格, 重要度)
    
    # 初始化dp数组，dp[i]表示预算为i时的最大满意度
    dp = [0] * (N + 1)
    
    # 遍历每个主件及其附件组合
    for main_id, v_main, p_main in main_items:
        for budget in range(N, v_main - 1, -1):
            # 只购买主件
            if budget >= v_main:
                dp[budget] = max(dp[budget], dp[budget - v_main] + v_main * p_main)
            
            # 购买主件和第一个附件
            if main_id in attach_items:
                if budget >= v_main + attach_items[main_id][0][1]:
                    dp[budget] = max(dp[budget], dp[budget - v_main - attach_items[main_id][0][1]] + v_main * p_main + attach_items[main_id][0][1] * attach_items[main_id][0][2])
                
                # 购买主件和第二个附件
                if len(attach_items[main_id]) > 1:
                    if budget >= v_main + attach_items[main_id][1][1]:
                        dp[budget] = max(dp[budget], dp[budget - v_main - attach_items[main_id][1][1]] + v_main * p_main + attach_items[main_id][1][1] * attach_items[main_id][1][2])
                    
                    # 购买主件和两个附件
                    if budget >= v_main + attach_items[main_id][0][1] + attach_items[main_id][1][1]:
                        dp[budget] = max(dp[budget], dp[budget - v_main - attach_items[main_id][0][1] - attach_items[main_id][1][1]] + v_main * p_main + attach_items[main_id][0][1] * attach_items[main_id][0][2] + attach_items[main_id][1][1] * attach_items[main_id][1][2])
    
    return dp[N]

# 读取输入
import sys
input = sys.stdin.read
data = input().strip().split('\n')
N, m = map(int, data[0].split())
items = [tuple(map(int, line.split())) for line in data[1:]]

# 计算并输出最大满意度
print(maximize_satisfaction(N, m, items))
