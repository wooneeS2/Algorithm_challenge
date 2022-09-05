from collections import defaultdict
import collections

def groupAnagrams(strs):
    #초기값이 없어도 추가를 할 수 있는 모듈
    hashmap = collections.defaultdict(list)
    
    for s in strs:
        hashmap["".join(sorted(s))].append(s)
    
    return hashmap.values()

print(groupAnagrams(['abc','bca','cba']))