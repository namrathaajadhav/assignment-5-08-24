#1.Write a program which will find all such numbers which are divisible by 7 but are not a 
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
#printed in a comma-separated sequence on a single line. 

numbers = []
for number in range(2000, 3200):
    if number % 7 == 0 and number % 5 != 0:
        numbers.append(str(number))

    print("," .join(numbers))


#2.With a given integral number n, write a program to generate a dictionary that contains (i, 
#i*i) such that is an integral number between 1 and n (both included). and then the program 
#should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
#the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

numbers = [1,2,3,4,5]
squares = {}
for number in numbers:
    squares[number] = number * number

    print(squares)


#3.Write a program which accepts a sequence of comma-separated numbers from console 
#and generate a list and a tuple which contains every number. Suppose the following input 
#is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
#'33', '12', '98'] ('34', '67', '55', '33', '12', '98')


numbers_str = input("Enter comma-separated numbers:")
numbers_list = numbers_str.split(",")
numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("tuple:", numbers_tuple)



#4.Write a program that accepts a comma separated sequence of words as input and prints 
#the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
#following input is supplied to the program: without, hello, bag, world Then, the output 
#should be: bag,hello,without,world

words = input("Enter comma-separated words:").split(",")
words.sort()
print(",".join(words))


#5.Write a program that accepts a sentence and calculate the number of letters and 
# digits. Suppose the following input is supplied to the program: hello world! 123 Then,
#  the output should be: LETTERS 10 DIGITS 3?

sentances = input("Enter a sentence:")
letters = sum(char.isalpha() for char in sentances)
digits = sum(char.isdigit() for char in sentances)

print("LETTERS", letters)
print("DIGITS", digits)


#6.Write a program that accepts a sentence and calculate the number of upper case letters 
# and lower case letters. Suppose the following input is supplied to the program: Hello 
# world! Then, the output should be: UPPER CASE 1 LOWER CASE 9


sentances = input("Enter a sentence:")
upper_count = sum(1 for char in sentances  if char.isupper())
upper_count = sum(1 for char in sentances if char.islower())


print("UPPER CASE", upper_count)
print("LOWER CASE",upper_count )

#7.Write a program that computes the net amount of a bank account based a transaction 
#log from console input.The transaction log format is shown as following: D 100 W 200 D means
#  deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300
#W 200 D 100 Then, the output should be: 500

def factorial(n):
    if n < 0:
        return "factorail does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *=  i
            return fact
number = int(input("Enter a number:"))
result = factorial(number)
print("The factorial of", number, "is", result)





#8.A website requires the users to input username and password to register. Write a program to check the
#validity of password input by users. Following are the criteria for checking the password: At least 1
#letter between [a-z] At least 1 number between [0-9] At least 1 letter between [A-Z] At least 1
#character from [$#@] Minimum length of transaction password: 6 Maximum length of transaction password: 
#12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

def factorial(n):
    if n < 0:
        return "factorail does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * 1
            return fact
number = int(input("Enter a numbers:"))
result = factorial(number)
print("The factorial of", number, "is", result)





#9.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are 
# square of keys.

def  generate_squares_dict():
    return{number: number **2 for number in range(1,21)}
squares_dict = generate_squares_dict()
print(squares_dict)




#10.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print
#  the last 5 elements in the list.

def generate_squares_list():
    squares = [number**2 for number in range(1,21)]
    return squares[-5:]
result = generate_squares_list()
print(result)
 
