import sys
input = sys.stdin.read
data = input().strip().split('\n')
N, m = map(int, data[0].split())
items = [tuple(map(int, line.split())) for line in data[1:]]

print(items)