# 부분 문자열(주어진 문자열에서 연속되는 맨 앞에서 부터 k개, 뒤에서 부터 l개(k + l < n)를 자른 문자열)
# 중에 팰린 드롬이 되는 제일 긴 문자열을 찾고,
# 그 문자열의 중심으로 부터 대칭되는 부분 문자열 역시 팰린드롬
def manacher(s):                # 입력: 문자열
    n = len(s)                  # 입력된 문자열의 길이
    p = [0] * n                 # 회문이 되는 길이를 저장하기 위한 리스트

    r = -1  # end of palindrome
    c = -1  # center of palindrome

    for i in range(0, n - 1):
        if r >= i:              # 회문이기 때문에 반대편도 똑같이 생겼다는 사실 이용
            p[i] = min(r - i, p[c * 2 - i])  # c + (c - i) symmetric point
        else:
            p[i] = 0

        while i + p[i] + 1 < n: # 회문의 길이 확인
            if s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            else:
                break

        if i + p[i] > r:        # 회문의 중심과 끝점 갱신
            r = i + p[i]
            c = i

    return p