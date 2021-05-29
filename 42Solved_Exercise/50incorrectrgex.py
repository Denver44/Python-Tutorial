# If we can compile any regx then it is a valid regular expression.
import  re
for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)