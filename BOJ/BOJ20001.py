stack = []

while True:
    N = input()
    if N == '문제':
        stack.append(1)
    elif N == '고무오리':
        if not stack:
            stack.append(1)
            stack.append(1)
        else:
            stack.pop()
    elif N == '고무오리 디버깅 끝':
        break

if not stack:
    print('고무오리야 사랑해')
else:
    print('힝구')