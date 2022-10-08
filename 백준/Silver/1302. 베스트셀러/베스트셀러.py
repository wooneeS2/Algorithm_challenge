import sys

input = sys.stdin.readline

num = int(input())

books={}

for _ in range(num):
        name = input().rstrip()
        if name in books:
                books[name]= books[name]+1
        else:
                books[name]=1

sorted_books = sorted(books.items(),key=lambda item:item[0])
max_value = max(books.values())

for key,value in sorted_books:
        if value==max_value:
                print(key)
                break

