# first solution

# N = int(input())
# words = []
# for _ in range(N):
#     word = input()
#     if word in words:
#         continue
#     else:
#         words.append(''.join(word))
# words.sort()
# words.sort(key=lambda x:(len(x)))
# for x in words:
#     print(''.join(map(str, x)))

# improved second
N = int(input())
words = set()
for _ in range(N):
   words.add(input())

for i in sorted(sorted(words), key=len):
    print(i)