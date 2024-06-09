'''
描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”

所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

数据范围：输入的字符串长度满足 1≤n≤1000 

注意本题有多组输入

输入描述：
输入一个英文语句，每个单词用空格隔开。保证输入只包含空格和字母。

输出描述：
得到逆序的句子
'''

def reverse_sentence(sentence):
    """
    将输入的英文语句以单词为单位逆序排放。

    :param sentence: 输入的英文语句
    :return: 逆序后的英文语句
    """
    # 将句子按照空格分割成单词列表
    words = sentence.split()
    # 将单词列表逆序
    reversed_words = words[::-1]
    # 将逆序后的单词列表拼接成一个新的句子
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

# 读取输入的多组英文语句
import sys
input_sentences = sys.stdin.read().strip().split('\n')

# 处理每一组输入并输出结果
for sentence in input_sentences:
    output_sentence = reverse_sentence(sentence)
    print(output_sentence)
