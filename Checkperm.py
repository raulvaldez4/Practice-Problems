#Given Two strings, write a method to decide if one is a permutation of the other
#Input: ('abcd','bacd')
#Output: True

#Input: ('dcw4f','dcw5f')
#Output: False

def checkperm(words):
    return sorted(words[0]) == sorted(words[1])