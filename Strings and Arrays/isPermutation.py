
testString = 'Hello my name is__'
uniqueString = 'abcdefghijklmnopqrstuvwxyz'


def isPermuation(stringOne, stringTwo):

    if len(stringOne) is not len(stringTwo):
        return False

    dictionary = {}
    dictionaryTwo = {}

    for x in stringOne:
        if x in dictionary:
            temp = dictionary[x]
            temp += 1
            dictionary[x] = temp
        else:
            dictionary[x] = 1
    
    for x in stringTwo:
        if x in dictionaryTwo:
            temp = dictionaryTwo[x]
            temp += 1
            dictionaryTwo[x] = temp
        else:
            dictionaryTwo[x] = 1

    for x in dictionary:
        if dictionary[x] is not dictionaryTwo[x]:
            return False

    return True

if __name__ == "__main__":
    print(isPermuation("aa", "aa"))
