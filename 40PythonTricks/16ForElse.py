num  =10

if num >1:

    for i in range(2,num):

        if (num%i) == 0:
            print(num,i,"is not a prime number")
            break;


    else: # this else is for and it is only run if the for loop dosnt terminate with break. else it will be going to rum at the end.
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
