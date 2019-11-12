
testString = 'Hello my name is__'
uniqueString = 'abcdefghijklmnopqrstuvwxyz'


def isUnique(string):
    traversed = []

    for x in string:
        if x in traversed:
            return False
        else:
            traversed.append(x)
    return True

def optimizedIsUnique(string):
    traversed = {}
    for x in range(len(string)):
        if string[x] in traversed:
            return False
        else:
            traversed[string[x]] = True
    return True

if __name__ == "__main__":
    print(optimizedIsUnique(testString))
    print(isUnique(uniqueString))
