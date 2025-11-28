def solve(N, A):
    """
    N: Represents the size of the array A
    A: Represents the elements of array A
    """
    S = sum(A)
    # If sum > 0, impossible (operations only increase total sum)
    if S > 0:
        return -1

    k = -S  # number of operations required to make total sum 0

    # compute required minimal f_i for negative A[i]:
    # need = sum( ceil((-A[i]) / 2) ) = sum( ( -A[i] + 1 ) // 2 )
    need = 0
    for x in A:
        if x < 0:
            need += ( -x + 1 ) // 2

    if need <= k:
        return k
    else:
        return -1


T = input()
for _ in xrange(T):
    N = input()
    A = map(int, raw_input().split())
    out_ = solve(N, A)
    print out_
