import random
print('Hello, what is your name?')
name = input()
top_of_range = 100

print(f'Well, {name} , I want you to guess what number I am thinking of between 1 and {top_of_range}.')

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print('You were below the number!')

print('You got it in', guesses, 'guesses')