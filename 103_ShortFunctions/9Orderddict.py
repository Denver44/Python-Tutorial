from collections import OrderedDict

dict1 = {}
dict1['a']= 1
dict1['b']= 2
dict1['c']= 3
dict1['e']= 5
dict1['d']= 4
dict1['d'] = dict1['d']+455
print(dict1)

dict2 = OrderedDict()

dict2['a']= 1
dict2['b']= 2
dict2['c']= 3
dict2['e']= 5
dict2['d']= 4
dict2['d']= 455
print(dict2)
