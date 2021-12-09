# Problem
# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
#
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

def compress(s):

    r = ""
    length = len(s)

    #Edge Case Check
    if length == 0:
        return ""

    if length == 1:
        return s+"1"

    # Algorithm

    # last = s[0] #Some people use last as a marker
    cnt = 1
    i = 1

    while i < length:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1

        i += 1
    r = r + s[i-1] +str(cnt)

    return r

# Testing

print(compress("AABaa"))
