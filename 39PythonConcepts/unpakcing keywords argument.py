def named(**kwargs):
    for arg,value in kwargs.items():
        print(arg,value)

dict1 = {"name":"Dugresh","age":21}
named(**dict1)

named( **{"name":"Vishal","age":21})
# named( **"name":"Vishal","age":21) This Will give Error