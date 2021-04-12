
'''
Coding Challenge 1: Palindrome Descendant
A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.

For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.

Create a function that returns true if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).

Examples
palindromedescendant(11211230) ➞ true
// 11211230 ➞ 2333 ➞ 56 ➞ 11

palindromeDescendant(13001120) ➞ true
// 13001120 ➞ 4022 ➞ 44

palindromeDescendant(23336014) ➞ true
// 23336014 ➞ 5665

palindromeDescendant(11) ➞ true
// Number itself is a palindrome.
Notes
Numbers will always have an even number of digits. 
'''
def palindromeDescendent(number):
  strNumber = str(number)

  if (len(strNumber) % 2) != 0:
    print("Number is uneven, cannot find palindrome descendent")
    return False
  
  if strNumber == strNumber[::-1]:
    return True

  newNumber = ""

  for i in range(0, len(strNumber), 2):
    newNumber += str(int(strNumber[i]) + int(strNumber[i+1]))

  print(newNumber)

  if newNumber == newNumber[::-1]:
    return True
  else:
    if len(newNumber) >= 2:
      return palindromeDescendent(int(newNumber))
    else:
      return False

'''
Coding Challenge 2: Next Largest Number
Write a function that returns the next number that can be created from the same digits as the input.

Examples
nextNumber(19) ➞ 91
nextNumber(3542) ➞ 4235
nextNumber(5432) ➞ 5432
nextNumber(58943) ➞ 59348

Notes
If no larger number can be formed, return the number itself.
Bonus: See if you can do this without generating all digit permutations. 
'''
def largestNumberPermutation(number):
  strNumber = str(number)
  numList = []
  for numb in strNumber:
    numList.append(numb)

  newNumber = ""

  while(numList):
    maxNum = max(numList)
    newNumber += str(numList.pop(numList.index(maxNum)))

  print(newNumber)

    

print(palindromeDescendent(1121123025))

#largestNumberPermutation("1291356")

