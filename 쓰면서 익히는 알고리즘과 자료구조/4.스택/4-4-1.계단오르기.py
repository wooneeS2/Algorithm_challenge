def climbStairs(n):
    def climb(n,i):
        if n==i:
            return 1
        if n<i :
            return 0
        return climb(n,i+1)+climb(n,i+2)
    return climb(n,0)

print( climbStairs(3))
