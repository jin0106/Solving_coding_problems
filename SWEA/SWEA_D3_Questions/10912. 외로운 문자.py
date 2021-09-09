# 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.
# 같은 문자를 여러 번 짝지어서는 안 된다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.
# 이 문자열의 길이는 1이상 100이하이다.

# [출력]
# 각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.
# 만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.

T = int(input())
for t in range(1, T+1):
    w = list(map(str, input()))      # 리스트로 입력 받기
    ans = []  # 답을 위한 빈 리스트 생성
    cnt = 0  # w가 있는지 없는지 확인하기 위해 생성
    for i in range(len(w)-1):   # w리스트를 완전탐색으로 똑같은 문자열이 있는지 확인 있으면 0으로 바꿈
        for j in range(i+1, len(w)):
            if w[i] == w[j]:
                w[i] = 0
                w[j] = 0
    for j in range(len(w)):  # 0이면 cnt에 +1, 0이 아니면 ans에 추가해줌
        if w[j] != 0:
            ans.append(w[j])
        else:
            cnt += 1
    if cnt == len(w):   # 위의 검사 결과, cnt가 w의 길이와 같으면 남은 문자가 없다는뜻이므로 Good을 출력
        print(f"#{t} Good")
    else:
        for x in range(len(ans)-1):  # cnt가 len(w)가 아니면 남은 문자가 있다는 뜻이므로 아스키코드 값으로 알파벳순으로 변경후 출력
            for y in range(x+1, len(ans)):
                if ord(ans[x]) > ord(ans[y]):
                    ans[x], ans[y] = ans[y], ans[x]
        print(f"#{t} {''.join(map(str, ans))}")
