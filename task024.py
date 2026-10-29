A = str(input())


def check(A):
    st = []
    for i in range(0,len(A)):
        if A[i] in '([{':
            st.append(A[i])
        elif A[i] in ')]}':
            if st and st[-1]+A[i] in '(){}[]':
                st.pop()
            elif not st:
                return False
    if not st:
        return True
    return False


if check(A):
    print('YES')
else:
    print('NO')
