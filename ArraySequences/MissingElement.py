# Problem
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
#
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
#
# Input:
#
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
#
# Output:
#
# 5 is the missing number

import collections

# Method 1

def finder(arr1, arr2):

    arr1.sort()
    arr2.sort()

    if len(arr1) == len(arr2):
        return "Length of both arrays is equal!"
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2 :
            return num1

    return arr1[-1]


# Method 2 => Applicable only for short arrays because summing long array is time consuming.

def finder2(arr1, arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    return sum1 - sum2


# Method 3 : Optimum DSA Solution

def finder3(arr1,arr2):

    d = collections.defaultdict(int)
    # print(d)

    for num in arr2:
        d[num] += 1

    # print(d)

    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1

# Method 4 : XOR method (A clever trick)

def finder4(arr1, arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num
        # print(result)

    return result

#Testing Method 1

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6,]
# print(finder(arr1, arr2))

#Testing Method 2

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,4,2,1,5,7]
# print(finder2(arr1, arr2))

#Testing Method 3

arr1 = [1,2,3,4]
arr2 = [3,4,2]
print(finder3(arr1, arr2))

#Testing Method 4

arr1 = [1,2,3,4]
arr2 = [3,4,2]
# print(finder4(arr1, arr2))

