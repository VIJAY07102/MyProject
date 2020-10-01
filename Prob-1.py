

# Implement an algorithm to determine if a string has all unique characters.

# Brute-force algorithm

def uniquechar(string):
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True

# Hash tables

def uniquechar1(string):
    dic = {}
    for char in string:
        if char not in dic:
            dic[char] = True
        else:
            return False
    return True

# Sorting method

def uniquechar2(string):
    string.sort()
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True


if__name__== '__main__':
    string = input('Enter the Charater Array:')
    print(uniquechar(string))