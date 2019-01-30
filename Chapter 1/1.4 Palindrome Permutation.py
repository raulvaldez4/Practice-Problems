# Given a string, write a solution to check if it is a permutation of a palindrome. A palindrome is a word or phrase
# that is the same forwards or backwards. A permutation is a rearrangement of letters. The palindrome does not need to
# be limited to just dict words

# Input: Tact Coa
# Output: True --> (perms: 'Taco cat', 'atco cta', etc.)

def palindrome_perm(string):
    string = str(string).replace(' ','').lower()
    letter_dict = {}

    for char in string:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    count = 0
    for index,value in letter_dict.items():
        if value %2 == 0:
            continue
        else:
            count += 1

    print(count)

    return count <= 1


print(palindrome_perm(''))