

def urlify(string, length):
    result = str()
    spaceReplacement = '%20'
    alreadyReplaced = False
    for x in string:
        if x is not ' ':
            if alreadyReplaced:
                result += spaceReplacement
                alreadyReplaced = False
            result += x
            # alreadyReplaced = False
        else:
            if not alreadyReplaced:
                # result += spaceReplacement
                alreadyReplaced = True

    return result


if __name__ == '__main__':
    print(urlify("Mr John Smith   ", 13))
