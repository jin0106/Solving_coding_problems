#
# priorities = list(map(int, input().split()))
# location = int(input())
# array1 = [c for c in range(len(priorities))]
#
# cnt = 0
# while len(priorities) > 0:
#     if priorities[0] < max(priorities):
#         priorities.append(priorities.pop(0))
#         array1.append(array1.pop(0))
#     else:
#         if array1[0] == location:
#             cnt += 1
#             print(cnt)
#             break
#         else:
#             priorities.pop(0)
#             array1.pop(0)
#             cnt += 1
arr = []
print(all(arr))