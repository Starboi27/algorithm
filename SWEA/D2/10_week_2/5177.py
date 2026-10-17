# 최소힙
# heap 배열 생성 0번 자리는 0으로 채움
# 새로운 인덱스 생성해야 됨 : now = len(heap) - 1
# 부모 위치 : i // 2

n = int(input())

for i in range(n):
    m = int(input())
    numbers = list(map(int, input().split()))
    heap = [0]

    for number in numbers:
        heap.append(number)
        now = len(heap) - 1

        while now > 1:
            parent = now // 2

            if heap[parent] <= heap[now]:
                break

            heap[parent], heap[now] = heap[now], heap[parent]

            now = parent

    print(heap)
