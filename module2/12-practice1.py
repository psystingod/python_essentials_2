def mysplit(strng):
    myList = [];
    word = "";
    if strng == "":
        return myList;
    for s in strng:
        if ord(s) != 32:
            word += s;
        elif ord(s) == 32:
            if word != "":
                myList.append(word);
            word = "";
    if word != "":
                myList.append(word);
    return myList;
        


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))