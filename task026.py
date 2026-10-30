import sys


def SAVE_ME_PLEASE(H,N):
    st = []
    ans = 0
    for hill in H:
        while st and st[-1][0] < hill:
            ans += st[-1][1]
            st.pop()
        if st:
            if st[-1][0]  == hill:
                ans += st[-1][1]
                if len(st) > 1:
                    ans+=1
                st[-1][1] +=1
            else:
                ans+=1
                st.append([hill,1])
        else:
            st.append([hill,1])
    print(ans)



def gr():
    V = sys.stdin.read().split()
    N = int(V[0])
    H = [int(x) for x in V[1:]]
    SAVE_ME_PLEASE(H,N)


if __name__ == '__main__':
    gr()