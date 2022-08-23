def solution(X, A):
    result = set()
    for i in range(len(A)):
        result.add(A[i])
        if len(result)==X:
            return i
    return -1