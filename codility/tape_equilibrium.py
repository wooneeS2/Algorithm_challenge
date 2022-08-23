# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    part_one = 0
    part_two=sum(A)
    min_difference = None

    for i in range(1,len(A)):
        part_one +=A[i-1]
        part_two -= A[i-1]
        difference = abs(part_one-part_two)

        if min_difference==None:
            min_difference=difference
        min_difference = min(min_difference,difference)
    return min_difference