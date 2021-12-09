# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
#
# For example:
#
# "public relations" is an anagram of "crap built on lies."
#
# "clint eastwood" is an anagram of "old west action"
#
# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

# Method 1

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

# Method 2 = More optimum way

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()

    #Edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

# Testing Method 1
print(anagram("dog", "god"))
print(anagram('clint eastwood', 'old west action'))

#Testing Method 2
print(anagram2("dog", "god"))
print(anagram2('clint eastwood', 'old west action'))