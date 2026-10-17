N = 6
numbers = [7, 2, 5, 3, 4, 6]

#   T = int(input())

#   for tc in range(1, T + 1):
#       N = int(input())
#       numbers = list(map(int, input().split()))

#       heap = [0]

#       # 최소힙 만들기
#       [7, 2, 5, 3, 4, 6]
#       for num in numbers:
#
#           heap.append(num)
#           [0, 2, 3, 4, 7, 5, 6]

#
#           child = len(heap) - 1
#           child = 6
#
#           while child > 1:
#               parent = child // 2
#               parent = 3

#               heap[4] = 2 < heap[6] = 6
#               if heap[parent] < heap[child]:
#                   break

#               heap[parent], heap[child] = heap[child], heap[parent]
#               child = parent
#               child = 3

#       # 마지막 노드의 조상 합 구하기
#       answer = 0
#       node = N // 2

#       while node >= 1:
#           answer += heap[node]
#           node //= 2

#       # 이번 테스트케이스 결과 출력
#       print(f"#{tc} {answer}")
