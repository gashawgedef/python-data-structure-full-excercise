


dict ={"gashaw":"Gedef","Shibabaw":"Tadege","Age":30}

for k, i in dict.items():
    print(k,i)


dict['Age']=31
dict['address'] = "Gondar"

def traverseDict(dict):
    for key in dict:
        print(key,dict[key])



def searchValue(dict,value):
    for key in dict:
        if dict[key] ==value:
            return key, value
    return "The Value Does not exist"
        
traverseDict(dict  )
print(searchValue(dict,31))
print(dict.pop('Age'))
print(dict.popitem() )
del dict['gashaw']
dict.clear()
dict1 = dict.copy()

print("Dictionary origional",dict)
print("Dictionary Copy",dict1)

newDict = {}.fromkeys([1,2,3],0)

print(newDict)
print(newDict.get(2))
print(newDict.items() )
print(newDict.keys())
print(newDict.values())

print( 0 in newDict.values())

