
def swap_case(s):
    str =''
    for i in range(len(s)):
        if s[i].isupper():
           str +=  s[i].lower()
        elif s[i].islower():
            str += s[i].upper()
        else:
            str += s[i]
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)