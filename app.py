import math
print("hellow world")

x = 555
print(x)

studentCount = 1000
rating = 4.33
isPublised = True

# working string

course = "pythong programing  "
# emailMessage = """
# Hi Dami

# my name is Dami and here to congratualte you for getting offer.
# """
# # print(emailMessage)
# print(len(course))
# print(course[-1])
# print(len(course[0:]))
# print(course)

# first = "Dami"
# last = "Fadodun"
# fullName =f"{first} {last}"
# print(fullName)
# print(course.upper())
# print(course.find("pr"))
# print(course.replace("th","TH"))
# print("th" in course)

# print (math.ceil(2.3))
# print(math.floor(2.3))
# print(math.fabs(-2.3))

# inputValue = input("x: ")
# inputValueToNumber = int(inputValue)
# y = inputValueToNumber + 6
# print(y)

# temperature = 12
# if temperature > 30:
#     print("ite's hot temperature")
#     print("drink water")
# elif temperature > 20:
#     print("it's mild temperature")
# elif temperature <= 15:
#     print("it's fine temperature")
# else:
#     print("it's cold temperature")

# age = 19
# message = "Eligable" if age > 18 else "you are not eligibale"

# print(message)


# high_income = True
# good_credit =  False

# if high_income and good_credit:
#     print("eligible for income: ")
# elif high_income or good_credit:
#     print("eligible for either income or credit")


# chaining comprisims
# age  = 19

# if 20 <= age  <60:
#     print("eligible for voters card")

# succfull = False
# for number in range(1, 9):
#     print("loading", (number), (number) * ".")
#     if succfull:
#         print("sent")
#         break
# else:
#     print("failed to send", number)

# list = []
# for x in range(1, 10):
#     if x % 2 == 0:
#         list.append(x)
#         print(f"{x}")
# else:
#     print(f"We have {len(list)} even numbers")

# def greet(first, last):
#     print(f"Hi there!, {first}:{last}")
#     print("Welcome to our program")

# greet("Damilare","Emmanuel" )

# def spreed(*params):
#     total = 1
#     for param in params:
#         total *= param
#         return total



# print("starting")
# spreed(1, 2, 3, 4, 5)

# def saveUser(**user):
#     print(user["email"])


# saveUser(name="Damilare", age=24, email="damilare@gmail.com")

# def fizzbuzz(param):
#     param = int(input(""))
#     if param % 3 == 0  and param % 5 == 0:
#         return "Fizzbuzz"
#     elif param % 3 == 0:
#         return "Fizz"
#     elif param % 5 == 0:
#         return "Buzz"
#     else: 
#         return param
    

# print(fizzbuzz(15))


def rolldice():
    x = random(1,10)
