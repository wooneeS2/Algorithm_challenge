
import sys

#크로아티아 알파벳을 모두 *로 치환해서 문자열의 개수를 세서 출력
word = (sys.stdin.readline()).replace('c=','*').replace('c-','*').replace("dz=","*").replace('d-','*').replace('lj','*').replace('nj','*').replace('s=','*').replace('z=','*').rstrip()
print(len(word))