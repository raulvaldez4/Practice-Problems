# Implement an algo to determine if a string has all unique characters
# Input: "test"
# Output: False
# Input: "abcd"
# Output: True

def isunique(word):
    word_dict = {}
    if len(word) == 0:
        return False
    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
    for index,value in word_dict.items():
        if value > 1:
            return False
        else:
            return True