from typing import List

def listavg(sequence : List)->int:
    return sum(sequence) // len(sequence)

print(listavg([1,2,3]))

#  The type hinting is given so that we that chances of error can be redueced