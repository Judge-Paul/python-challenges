import math
# 10 Python Code Challenges for Beginners - www.codecademy.com/resources/blog/python-code-challenges-for-beginners
# Question 1 - Convert Radians into degrees
print("10 Python Code Challenges for Beginners")
print("Question 1")


def temp_conv(radian):
    degree = radian * (180 / math.pi)
    return degree


print(f"90 Radian is equal to {temp_conv(90)} degrees.")

# Question 2 - Sort a list
print("Question 2")


def list_arrng(list1, method):
    if method == "asc":
        list1.sort()
    elif method == "desc":
        list1.sort(reverse=True)
    elif method == "none":
        list1 = list1
    return list1


print(f"The list in ascending order is {list_arrng([42, 34, 8, 2, 7, 43, 1, 21, 45], 'asc')}")
print(f"The list in descending order is {list_arrng([42, 34, 8, 2, 7, 43, 1, 21, 45], 'desc')}")
print(f"The list in its original order is {list_arrng([42, 34, 8, 2, 7, 43, 1, 21, 45], 'none')}")

# Question 3 - Convert a decimal into binary
print("Question 3")


def bin_conv(dec):
    binary = []
    bin_str = ""
    while dec > 0:
        dec1 = dec % 2
        dec = dec // 2
        binary.append(dec1)
    binary.reverse()
    for num in binary:
        bin_str += str(num)
    return bin_str


print(f"The binary form of 15 is {bin_conv(15)}")

# Question 4 - Count the vowels in a string
print("Question 4")


def vowel_count(word):
    vowel = 0
    for letter in word.lower():
        if letter == "a":
            vowel += 1
        elif letter == "e":
            vowel += 1
        elif letter == "i":
            vowel += 1
        elif letter == "o":
            vowel += 1
        elif letter == "u":
            vowel += 1
    return vowel


print(f"There are {vowel_count('Alphabet')} vowels in the word 'Alphabet'")

# Question 5 - Hide the credit card number
print("Question 5")


def cc_num_count(numbers):
    nums = []
    num = ""
    for number in str(numbers):
        nums.append(number)
    for digit in nums[12:]:
        num += str(digit)
    return num


print(f"The last digits of the credit card are {cc_num_count(5348173217381938)}")

# Question 6 - Are the Xs equal to the Os?
print("Question 6")


def x_equal_o(string):
    x = 0
    o = 0
    for char in string.lower():
        if char == "x":
            x += 1
        elif char == "o":
            o += 1
    if x == o:
        chk = True
    else:
        chk = False
    return chk


x_equals_o = x_equal_o("xxxxdsdoooofsfa")
print(x_equals_o)
if x_equals_o:
    print("The number of Xs in the phrase are equal to the number of Os")
else:
    print("The number of Xs in the phrase are not equal to the number of Os")

# Question 7 - Create a calculator function
print("Question 7")


def calculate(num1, sign, num2):
    result = 0
    if sign == '+':
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "*":
        result = num1 * num2
    elif sign == "/":
        result = (num1 / num2)
    return result


print(f"20 + 10 = {calculate(20, '+', 10)}")
print(f"20 - 10 = {calculate(20, '-', 10)}")
print(f"20 * 10 = {calculate(20, '*', 10)}")
print(f"20 / 10 = {calculate(20, '/', 10)}")

# Question 8 - Give me the discount
print("Question 8")


def discount_getter(price, discount):
    result = int(price - (price * (discount / 100)))
    return result


print(f"At a 20% discount $100 will be ${discount_getter(100, 20)}")


# Question 9 - Just the numbers
print("Question 9")


def only_numbers(varchar):
    integers = []
    for variable in varchar:
        if type(variable) == int:
            integers.append(variable)

    return integers


print(f"The Integers in this list are {only_numbers(['hello', 39, 'Alan', 9.31, 'Dane', 12, 123, 11, 'Bob', 'Alan'])}")


# Question 10 - Repeat the characters
print("Question 10")


def character_repeat(word):
    word_list = ""
    for char in word:
        word_list += char*2

    return word_list


print(character_repeat('123a'))
print(character_repeat('now'))
