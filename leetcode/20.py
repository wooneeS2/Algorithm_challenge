class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        parentheses={
            ')':'(',
            '}':'{',
            ']':'['
        }   
        for p in s:
            if p not in parentheses.keys():
                result.append(p)
            else:
                pair = result.pop() if result else ''
                
                if parentheses[p] != pair:
                    return False
        return len(result)==0
    
    stack = []
    
   