
import sys

word = (sys.stdin.readline()).replace('c=','*').replace('c-','*').replace("dz=","*").replace('d-','*').replace('lj','*').replace('nj','*').replace('s=','*').replace('z=','*').rstrip()
print(len(word))