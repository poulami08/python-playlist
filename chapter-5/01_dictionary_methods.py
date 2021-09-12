myDict ={
    "fast":"in a quixk manner",
    "marks": [1,2,3],
    "another": {"harry":"me"},
    1:2
}

print(myDict['fast'])
print(myDict['marks'])
print(myDict['another']['harry'])


# methods

print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))

print(myDict.values())

print(myDict.items())

print(myDict)
updateDict={
    "lovish" : "friend",
    "me" : "myself",
    "fast" :"speed"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry"))
#we use get method because if the key was not present in the dictionary then it will print none,
# where as in print(myDict["harry"]) if the key was not present then it will give an error.
# But if the key was present in the list then both will work.
