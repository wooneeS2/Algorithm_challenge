import sys


num = int(sys.stdin.readline())
cards = {}

for _ in range(num):
        card = int(sys.stdin.readline().rstrip())
        if card in cards:
                cards[card] = cards[card]+1
        else:
                cards[card]=1

max_value = (max(cards.values()))

sorted_cards = sorted(cards.items(),key=lambda item:item[0])

for key,value in sorted_cards:
        if value==max_value:
                print(key)
                break
                