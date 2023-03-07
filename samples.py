
# #Day 1 Prefix Sum
# #start at index 0
# #take sum to the left - 
# #take sum to the right
# #do not include current index
# #if they equal, return current index
# def pivotIndex(nums):
#     totalSum = sum(nums)
#     leftSum = 0
#     for i in range(len(nums)):
#         if leftSum == totalSum - leftSum - nums[i]:
#             return i
#         leftSum += nums[i]
#     return -1
    
# nums = [1,7,3,6,5,6] 
# print(pivotIndex(nums))
#--------------------------------------------------------

#Day 2 - String
#loop through each string, if the character isn't equal to anything in there, give a 0
#if it is the same as another,give it the same number
#do for both strings
#if lists are equal, they are isomporhic
# def isIsomorphic(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
        
#     s_to_t = {}
#     t_to_s = {}
#     for i in range(len(s)):
#         if s[i] not in s_to_t and t[i] not in t_to_s:
#             s_to_t[s[i]] = t[i]
#             t_to_s[t[i]] = s[i]
#         elif s[i] in s_to_t and s_to_t[s[i]] == t[i]:
#             continue
#         else:
#             return False
            
#     return True

# s = "egg" 
# t = "add"
# print(isIsomorphic(s,t))

#--------------------------------------------
#2 sum in an array problem SOLVED

# numbers= [4, 1, 5, 0, -1]
# target= 10
# def twoSum(numbers, target):
#     for i in range(len(numbers)):
#         dif = target - numbers[i]
#         if numbers.count(dif) == 1:
#             index = numbers.index(dif)
#             if numbers[index] == numbers[i]:
#                 continue
#             return i, index
#     return -1, -1

# print(twoSum(numbers, target))

#------------------------------------
#add one problem SOLVED
# def addOne(digits):
#     combinedDigits = ""
#     finalArray = []
#     for i in range(len(digits)):
#         combinedDigits += str(digits[i])
#     numberPlusOne = int(combinedDigits) + 1
#     stringNumberPlusOne = str(numberPlusOne)
#     for i in range(len(stringNumberPlusOne)):
#         finalArray.append(int(stringNumberPlusOne[i]))
#     return finalArray

# digits = [9,9,9]
# print(addOne(digits))

#------------------------
#3 sum smaller problem
#start at first index
# def threeSum(target, numbers, n):
#     answer = 0
#     for i in range(0, n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1,n):
#                 if numbers[i] + numbers[j] + numbers[k] < target:
#                     answer +=1
#     return answer
# target = 7
# numbers = [2,2,2,1]
# n = len(numbers)
# print(threeSum(target, numbers, n))


#--------------------------
#5 add strings problem
# def addStrings(strA, strB):
#     intA = int(strA)
#     intB = int(strB)
#     sum = intA + intB
#     return str(sum)

# strA= "1000"
# strB = "22"
# print(addStrings(strA, strB))

#--------------------------
#6 Zigzag sort problem
# def zigZag(numbers):
#     zigZagList = []
#     bigToSmall = numbers.sort(reverse=True)
#     listLength = len(numbers)
#     largeNumberIndex = 0
#     smallNumberIndex = len(numbers)-1
#     for i in range(len(numbers)):
#         if (i%2) == 0:
#             zigZagList.append(numbers[smallNumberIndex])
#             smallNumberIndex -=1
#         else:
#             zigZagList.append(numbers[largeNumberIndex])
#             largeNumberIndex +=1
#     return zigZagList

# numbers = [3, 1, 3, 1, 2, 4]
# print(zigZag(numbers))

#--------------------------
# #7 Merge two sorted lists

# def mergeTwoLists(list1,list2):
#     mergedList = list1 + list2
#     mergedList.sort()
#     return mergedList

# list1 = []
# list2 = [0]

# print(mergeTwoLists(list1, list2))

#--------------------------
# #8 reverse a linked list
#solved in leetcode, copied and pasted code here.
def reverseList(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

print(reverseList([1,2]))