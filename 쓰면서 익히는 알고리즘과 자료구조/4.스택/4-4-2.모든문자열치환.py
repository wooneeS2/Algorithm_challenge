
res=[]
def find_permutation(chs, s, e):
    if s==e -1:
        res.append("".join(chs))
    else:
        for i in range(s,e):
            chs[s],chs[i] = chs[i],chs[s]
            find_permutation(chs,s+1,e)
            chs[s],chs[i] = chs[i],chs[s]

s='abc'
find_permutation(list(s),0,len(s))
print(*res)

'''

def find_permutation(s):
    if len(s)==1:
        return list(s)
    
    ans=[]
    curr=s[0]
    s=s[1:]
    
    word = find_permutation(s)
    
    for sub in word:
        for i in range(len(sub)+1):
            ans.append("".join([sub[:i],curr,sub[i:]]))
    return ans
    
s='abc'

res=find_permutation(s)
print(*res)

'''