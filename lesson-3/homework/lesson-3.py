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

animals = ("tiger", "elephant", "eagle", "giraffe", "bear", "lion")

print(animals.index("lion"))                                  # "index" method returns the index of the elemen taken as argument

# 11.

num1 = (1, 4, 8)

num2 = (3, 6, 4)

num1 += num2                                                # merging the two tuples using + operator

print(num1)

# 12.

num1_t = (1, 4, 8)

num2_l = [3, 6, 4]

print(len(num1_t))                                        # len function is used to count the length of both tuple and list
print(len(num2_l))

# 13.

num1 = (1, 4, 8, 3, 5)

num2 = list(num1)

print(type(num2))

# 14.

num1 = (1, 4, 8, 3, 5)

max = max(num1)

min = min(num1)

print(f"The maximum is {max} and the minimum is {min}.")

# 15. 

num1 = ("good", "ok", "bad")

num2 = tuple(reversed(num1))

print(num2)





