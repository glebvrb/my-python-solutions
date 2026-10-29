import sys
A = str(sys.stdin.readline())


def check(A):
    st=[]
    cnt=0
    for i in range(len(A)):
        if A[i] in '{[(':
            st.append(A[i])
        elif A[i] in '}])':
            if st:
                if st[-1] + A[i] in '{}[]()':
                    st.pop()
                else:
                    cnt+=1
                    st.pop()

            elif not st:
                return -1
    if not st:
        return cnt
    return -1

print(check(A))
