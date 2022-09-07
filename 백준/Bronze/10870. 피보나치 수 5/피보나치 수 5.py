import sys

N = int(sys.stdin.readline())


def fibo(N):
    if N<=1:
        return N
    return fibo(N-1)+fibo(N-2)

print(fibo(N))
     