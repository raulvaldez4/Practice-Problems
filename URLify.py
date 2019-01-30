#1.3 Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold
#the add'l characters, and that you are given the 'true' length of the string. 

def URLify(word,n):
    new_word = []
    for letter in word:
        if letter == ' ':
            new_word.append('%20')
        else:
            new_word.append(letter)
    return ''.join(new_word[:n])
