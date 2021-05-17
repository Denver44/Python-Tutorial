
def decor_result(result_function):
    def distinction(marks1,name):
        for m in marks1:
            if m >= 75:
                print("DISTINCTION")
        result_function(marks1,name)

    return distinction


@decor_result
def result(marks, name):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("Fail")
            break

    else:
        print("PASS")


result([50, 60, 70, 80, 90], ["D", "V", "S"])
