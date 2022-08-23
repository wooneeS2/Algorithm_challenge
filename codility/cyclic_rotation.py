from collections import deque

def solution(A, K):
    queue = deque()
    for i in A:
        queue.append(i)
    queue.rotate(K)
    return(list(queue))
