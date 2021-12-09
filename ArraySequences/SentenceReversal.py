# Problem
# Given a string of words, reverse all the words. For example:
#
# Given:
#
# 'This is the best'
#
# Return:
#
# 'best the is This'
#
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
#
# '  space here'  and 'space here      '
#
# both become:
#
# 'here space'

# Method 1 : Short trick

def rev_word1(s):
    return " ".join(reversed(s.split()))

# Method 2 : Short trick

def rev_word2(s):
    return " ".join(s.split()[::-1])

# Method 3 : Optimum DSA solution

def rev_word3(s):

    words = []
    length = len(s)
    spaces = [' ']

    i = 0

    #Coding manually split functionality
    while i < length:

        if s[i] not in spaces:

            word_start = i

            while i < length and  s[i] not in spaces:

                i += 1

            words.append(s[word_start:i])
            # print(words)

        i += 1

    return " ".join(reversed(words))



# Testing Method 1

# print(rev_word1('This is the best'))

#Testing Method 2

# print(rev_word2('This is the best'))

# Testing Method 3

print(rev_word3('This is the best'))
print(rev_word3("     Hello how   are you"))