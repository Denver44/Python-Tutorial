# n,m = map(int,input().split())
#
# s = "WELCOME"
# s1 ='.|.'
#
#
# middle = n//2
# for i in range(middle):
#     print((s1*((i*2)+1)).center(m,'-'))
#
# print(s.center(m,'-'))
#
# middle = middle -1
# for i in range(middle,-1,-1):
#     print((s1*((i*2)+1)).center(m,'-'))

s1 = '*'
for i in range(3):
    print((s1*((i*2)+1)).center(21,))
for i in range(3,-1,-1):
    print((s1*((i*2)+1)).center(21,))