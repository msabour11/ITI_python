# # print('hello')
# # print('hello')
# # for i in range(3):
# #     print(i)



# # write function that calculates the prime number
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(2))
# l1=[1,2,3]
# l2=l1
# l2.append(6)
# print(l1)
# i=0
# message =input('Please enter string ')
# for x in message:
#     if x in ['a','i','e','u','o']:
#         i=i+1
# print(i)


# 2

# elements = []


# for i in range(5):
#     element = int(input(f"Enter element {i + 1}: "))
#     elements.append(element)


# ascending_sorted = sorted(elements)


# descending_sorted = sorted(elements, reverse=True)
# print(ascending_sorted,descending_sorted)



# 3
# text = input("Enter a string: ")


# count = text.count("iti")


# print( count)



# 4

# input_word = input("Enter a word: ")

# brief_version = ""
# vowels = "aeiouAEIOU"

# for char in input_word:
#     if char not in vowels:
#         brief_version += char

# print("version without vowels:", brief_version)


# 5


# input_string = input("Enter a string: ")

# locations = []

# for index, char in enumerate(input_string):
#     if char == 'i':
#         locations.append(index)

# print(locations)


# 6
lines=input('Enter number of lines: ')
if lines.isdigit():
    lines=int(lines)
    for i in range(lines):
        print()
        for j in range(i+1):
            print("*", end="")
    print()
else:
    print("Invalid input string must be a number")
