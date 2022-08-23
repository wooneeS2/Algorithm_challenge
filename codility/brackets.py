def solution(S):
    brackets = {"(":")", "{":"}", "[":"]"}
    stack = []

    for char in S :
        if brackets.get(char,False):
            stack.append(char)
        else:
            if not stack or brackets[stack.pop()] != char: return 0
    if stack: return 0
    else:
        return 1