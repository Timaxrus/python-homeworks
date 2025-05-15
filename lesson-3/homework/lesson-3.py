# 1.

fruits = ["apple", "orange", "banana", "grape", "cherry"]

print(fruits[2])                                    # accessing the 3rd element of the list

# 2.

num1 = [1, 3, 6]

num2 = [2, 4, 8]

num1.extend(num2)                                  # concatinating the two lists using "extend" list method

print(num1)

# 3.

num1 = [1, 3, 6, 5, 2, 4, 8]

num2 = [num1[0], num1[len(num1) // 2], num1[-1]]            # accessing the first, middle and last elements of the num1 list and assigning them to a new list named num2

print(num2)

# 4.

movies = ["Titanic", "The Equlizer", "Low Abiding Citizen"]

movies2 = tuple(movies)                                     # converting the list into a tuple using tuple constructor

print(type(movies2), movies2, sep = "\n")

# 5.

cities = ["London", "Paris", "Tashkent", "Amsterdam"]

city = "Paris"                                              # assigning "Paris" ot a variable called city so that we can use the variable in the output dynamically


if city in cities:
  print(f'{city} exists in the list.')                     # the output message if the city value exists in the list
else:
  print(f'{city} does not exist in the list')              # the output message if the city value does not exist in the list

# 6.

num1 = [3, 5, 7, 9, 10]

num2 = num1.copy()                                       # duplicating the num1 list using the copy list method

print(num2)

# 7.

num1 = [3, 5, 7, 9, 10]

num1[0], num1[-1] = num1[-1], num1[0]

print(num1)

# 8.

num1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(num1[3:8])                                       # accessing elements at indices from 3 to 7

# 9.

num1 = ["white", "blue", "red", "yellow", "blue", "purple"]

color = "blue"                                                   # assigning the color 'blue' to color variable so that it can be changed and used dynamically

count = num1.count(color)                                       # counting the occurance of "color" in the list.

print(f"The color '{color}' appears in the list {count} times.")            # using f-string to dynamically access the variables.


# 10.






