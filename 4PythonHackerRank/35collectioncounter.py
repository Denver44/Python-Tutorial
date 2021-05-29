from collections import Counter

number_of_shoe = int(input())
list1 = list(map(int, input().split(' ')))
number_of_cutomer = int(input())

record = Counter(list1)

total_sell = 0
for i in range(number_of_cutomer):
    customer = list(map(int, input().split()))
    if record[customer[0]] > 0:
        total_sell += customer[1]
        record[customer[0]] -= 1

print(total_sell)
