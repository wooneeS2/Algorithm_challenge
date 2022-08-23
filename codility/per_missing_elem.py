def solution(A):
    N = len(A)+1
    range_sum = N*(N+1)/2
    array_sum = sum(A)
    return int(range_sum-array_sum)