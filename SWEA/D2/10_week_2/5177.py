# 최소힙
# heap 배열 생성 0번 자리는 0으로 채움
# 새로운 인덱스 생성해야 됨 : now = len(heap) - 1
# 부모 위치 : i // 2

import sys

sys.stdin = open(r"C:\Users\dlckd\알고리즘\SWEA\D2\10_week_2\sample_input.txt", "r")


def SUM(node):

    global result

    if node <= 0:
        return
    SUM(node // 2)
    result += heap[node]

    return result


t = int(input())

for tc in range(1, t + 1):
    NodeNum = int(input())
    Nodes = list(map(int, input().split()))
    heap = [0]

    for Node in Nodes:
        heap.append(Node)
        now = len(heap) - 1

        while now > 1:
            parent = now // 2

            if heap[parent] < heap[now]:
                break

            heap[parent], heap[now] = heap[now], heap[parent]
            now = parent
    result = 0
    lastNode = (len(heap) - 1) // 2

    print(f"#{tc} {SUM(lastNode)}")
