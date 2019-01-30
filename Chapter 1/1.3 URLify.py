def URLify(word,n):
    new_word = []
    for letter in word:
        if letter == ' ':
            new_word.append('%20')
        else:
            new_word.append(letter)
    return ''.join(new_word[:n])