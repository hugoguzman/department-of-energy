
# REVERSE A STRING :
rev_test = 'Hugo'
def FirstReverse(str):
    return str[::-1]

# keep this function call here
print('FirstReverse:', FirstReverse(rev_test)) # leirbaG

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# FACTORIAL : takes num param and returns the factorial >> For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24

def FirstFactorial(num):
    total = 1
    while num > 0:
        total *= num
        num -= 1
    return total

print('FirstFactorial:', FirstFactorial(4))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LONGEST WORD : takes sen param and returns largest word in the string. If two words are the same length, return the first one
import re # regex import
def LongestWord(sen):
    longest = ''
    for word in sen.split(' '):
        word = re.sub(r"[^A-Za-z]+", '', word) # removes anything not in the regex
        if len(word) > len(longest):
            longest = word
    return longest

print('LongestWord(sen):', LongestWord('This is a sentence with multiple words in it'))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LETTER CHANGES : take a str param and replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
def LetterChanges(str):
    new_word = ""
    for char in str:
        next_letter = chr(ord(char) + 1) if char.isalpha() else char # return next letter or whatever the char is (not a letter)
        if next_letter in ['a', 'e', 'i', 'o', 'u']:
            next_letter = next_letter.upper()
        new_word += next_letter
    return new_word

# NOTES : ord(char) == gets the ascii of a letter // char.isalpha() checks whether letter is in alphabet // returns BOOL of >> is next_letter in ['a', 'e', 'i', 'o', 'u']
print(LetterChanges('gabe'))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Letter Capitalize
# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space.

def LetterCapitalize(strParam):
  cap_str_array = [word.capitalize() for word in strParam.split(' ')]
  return ' '.join(cap_str_array)


print(LetterCapitalize('hello world'))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Simple Symbols
# take the str param and determine if it is an acceptable sequence by either returning the string true or false.
# The str parameter will be composed of + and = symbols with several characters between them
#  to be true each letter must be surrounded by a + symbol.
import re # regex import
def SimpleSymbols(strParam):
    result = 'true'

    for i in range(len(strParam)):
        if (strParam[i].isalpha()):
            if (i < 1 or (strParam[i - 1] != '+' or strParam[i + 1] != '+')):
                result = 'false'
    return result

# keep this function call here
print(SimpleSymbols('==+f+==3==+N+'))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Simple Adding
# Have the function SimpleAdding(num) add up all the numbers from 1 to num.
def SimpleAdding(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

print(SimpleAdding(4)) # 1 + 2 + 3 + 4 = 10

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Time Convert
# take a num as the param and returns the number of hours and minutes converted (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.
import math
def TimeConvert(num):
    hours = math.floor(num / 60)
    mins = num % 60
    return f'{hours}:{mins}'

print(TimeConvert(63))

# Input: 126 // Output: 2:6
# Input: 45 // Output: 0:45

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Alphabet Soup
# takes a str string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo).
def AlphabetSoup(str):
    strArr = list(str)
    strArr.sort()
    return ''.join(strArr)

print(AlphabetSoup('hello'))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Vowel Count
# takes a string and returns the number of vowels the string contains.
def VowelCount(str):
    count = 0
    for char in str.lower():
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

print(VowelCount("All cows eat grass and moo")) # 8

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Word Count
# takes a string and returns the number of words the string contains
# (e.g. "Never eat shredded wheat or cake" would return 6).

def WordCount(str):
    return len(str.split(' '))

print(WordCount("Never eat shredded wheat or cake")) # 6

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Check Nums
# CheckNums(num1,num2) takes 2 params and return the string true if num2 is greater than num1, otherwise return the string false.
# If the parameter values are equal to each other then return the string -1.

def CheckNums(num1,num2):
   if num1 == num2:
       return '-1'
   else:
       return 'true' if num2 > num1 else 'false'

print(CheckNums(2,1))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# AB Check
# takes a str parameter and returns the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once
# (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.

def ABCheck(str):
    str.lower()
    for i in range(len(str)):
        if i + 4 < len(str):
            if str[i] == 'a' and str[i + 4] == 'b' or str[i] == 'b' and str[i + 4] == 'a':
                return 'true'
    return 'false'

print(ABCheck("123advb"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Ex Oh
# takes a string and returns 'true' if there is an equal number of x's and o's, otherwise returns 'false'.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.
def ExOh(str):
    str.lower()
    xCount = 0
    oCount = 0
    for char in str:
        if char == 'x':
            xCount += 1
        elif char == 'o':
            oCount += 1
    return  'true' if xCount == oCount else 'false'

print(ExOh("xooxxxooxo")) # true
print(ExOh("xooxxxxooxo")) # false

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Palindrome
# takes a str param and returns the string true if the param is a palindrome, (the string is the same forward as it is backward) otherwise return the string false.
# For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string.
def palindrome(str):
    test_str = ''.join(str.split(' '))
    return 'true' if test_str == test_str[::-1] else 'false'

print((palindrome( "never odd or even"))) # true
print((palindrome( "test"))) # false

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Arith Geo
# takes array of numbers and returns the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
# If the sequence doesn't follow either pattern return -1.
# An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio.
# Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

def ArithGeo(arr):

    def is_arithmetic(arr):
        prev_value = 0
        prev_diff = 0
        for i in range(len(arr)):
            if i == 0:
                prev_value = arr[i]
            elif i == 1:
                prev_diff = prev_value % arr[i]
                prev_value = arr[i]
            else:
                curr_diff_value = arr[i] % prev_value
                if prev_diff != curr_diff_value:
                    return False
                prev_diff = curr_diff_value
                prev_value = arr[i]
        return True

    def is_geometric(arr):
        prev_value = 0
        prev_diff = 0
        for i in range(len(arr)):
            if i == 0:
                prev_value = arr[i]
            elif i == 1:
                prev_diff = prev_value / arr[i]
                prev_value = arr[i]
            else:
                curr_diff_value = arr[i] / prev_diff
                if prev_diff != curr_diff_value:
                    return False
                prev_diff = curr_diff_value
                prev_value = arr[i]
        return True


    if is_arithmetic(arr):
        return "Arithmetic"
    elif is_geometric(arr):
        return "Geometric"
    else:
        return -1

result = ArithGeo([2,4,16,24])
print(result)

# 1. For input [2,6,18,54] the output was incorrect. The correct output is Geometric
#
# 2. For input [100,200,400,800,1600] the output was incorrect. The correct output is Geometric
#
# 3. For input [10,110,210,310,410] the output was incorrect. The correct output is Arithmetic
#
# 4. For input [5,10,20,40,80] the output was incorrect. The correct output is Geometric
#
# 5. For input [-3,-4,-5,-6,-7] the output was incorrect. The correct output is Arithmetic
#
# 6. For input [1,5,9] the output was incorrect. The correct output is Arithmetic

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -