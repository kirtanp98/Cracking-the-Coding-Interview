def isPermutation(string):
    string = string.replace(" ", "").lower()

    dicti = {}

    print(string)
    for x in string:
        print(x)
        if x in dicti:
            temp = dicti[x]
            temp += 1
            dicti[x] = temp
        else:
            dicti[x] = 1

    oneOdd = False

    for i in dicti:
        if (dicti[i] % 2 == 0):
            continue
        else:
            if not oneOdd:
                oneOdd = True
            else:
                return False

    return True


if __name__ == '__main__':
    print(isPermutation("Tact Coa"))
