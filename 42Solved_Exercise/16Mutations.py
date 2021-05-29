# #  FIRST METHOD
#
# a = "durgesh"
# l =list(a)
# l[0] = 'M'
# a = ''.join(l)
# print(a)
#
#
# # SECOND METHOD
# b=  "vishal"
# c = b[0:3] + 'd'+ b[4:]
# print

def mutate_string(string, position, character):
    newstr = string[0:position] + character + string[position+1 :]
    return newstr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)