import json

data = '{"var1":"harry","var2":56}'

parsed = json.loads(data)  # it help us to parsed a string in json.
print(parsed['var1'])
print(parsed['var2'])
print(type(parsed))
# Now this is parsed in Json type.


data2 = {"channel_name": "easycode", "cars": [
    'BMW', "AUDI Q3"]}


jscomp = json.dumps(data2)
print(jscomp)
print(type(jscomp))
