def minion_game(string):
    Sturat = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', "U"]:
            Kevin += len(string) -i
            print((len(string) - i))
        else:
            Sturat +=  len(string) -i

    if (Sturat == Kevin):
        print("Draw")
    elif (Sturat > Kevin):
        print("Stuart", Sturat)
    else:
        print("Kevin", Kevin)

if __name__ == '__main__':
    s = input()
    minion_game(s)