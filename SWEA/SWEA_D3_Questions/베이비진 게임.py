T = int(input())

# def triplet(lst):
#     global ans
#     for i in range(len(lst)):
#         if lst.count(lst[i]) >= 3:
#             return True
#
#
# def runn(lst):
#     global ans
#     lst.sort()
#     for i in range(len(lst)-2):
#         if lst[i]+1 == lst[i+1] and lst[i]+2 == lst[i+2]:
#             return True
#
def check(lst):
    if len(lst) <3:
        return
    card = [0]*10
    for i in range(len(lst)):
        card[lst[i]] +=1
    for j in range(8):
        if card[j] >=3:
            return True
        if card[j] and card[j+1] and card[j+2]:
            return True
    return False


T = int(input())
    for t in range(1, T+1):
        arr = list(map(int, input().split()))
        a = []
        b = []
        ans = 0
        for i in range(len(arr)):
            if i % 2 ==0:
                a.append(arr[i])
                if check(a):
                    ans = 1
                    break
                # if triplet(a) or runn(a):
                #     ans = 1
                #     break
            else:
                b.append(arr[i])
                if check(b):
                    ans=2
                    break
                # if triplet(b) or runn(b):
                #     ans = 2
                #     break

        if not ans:
            print(f'#{t} {ans}')
        else:
            print(f'#{t} {ans}')

