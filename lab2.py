# words=['java','python','php','per','cpp','sql','sqlite',]
# import random

# choise=random.choice(words)

# print(choise)
# name=input("Enter Your Name ").capitalize()

# print(f'Hello {name}')

# tries=3
# while tries:
#     guess=input("Enter Your guess programming language ").lower()
#     if guess == choise:
#         print(f'Congrats {name} you have guessed {guess}')
#         break

#     elif tries>0 :
#         print(f'Try again {name}')
    
#     else :
#           print(f'Sorry {name} you are out of tries')
#     tries=tries-1
    

import random

language = ['java', 'python', 'php', 'perl', 'cpp', 'sql', 'sqlite']
choice = random.choice(language)

print(choice)
name = input("Enter Your Name ").capitalize()
print(f'Hello {name}')
print('please guess from shown language')
for i ,j in enumerate(language):
        print(f'{i+1} ==> {j}')
tries = 3
while tries:
    
    guess = input("Enter Your guess programming language ").lower()
    if guess == choice:
        print(f'Congrats {name} you have guessed {guess}')
        break
    else:
        print(f'Try again {name}')
        tries = tries - 1

if tries == 0:
    print(f'Sorry {name} you are out of tries')

