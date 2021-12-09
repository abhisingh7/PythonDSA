# Problem
# # Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

# Method 1 : Short trick
def uni_char(s):
    return len(set(s)) == len(s)

# Method 2 : DSA Solution

def uni_char2(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

# Testing Method 1

# print(uni_char("abhi"))
# print(uni_char("aabc"))

# Testing Method 2

print(uni_char("abhi"))
print(uni_char("aabc"))