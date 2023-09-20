import random
import hangman_art
import hangman_word

word = random.choice(hangman_word.word_list)
# print(word)

display_lst = list(word)

# hangman_ctr keeps track the number of failures (failure limit == 9)
hangman_ctr = 6
full_life = 6
# right_guess helps while loop to break if the user guesses right before reaching failure limit(9)
right_guess = 0

# display ascii art
print(hangman_art.logo)
# answer_list = ['_'] * 2 -> you can put anything you want in []
answer_list = ['_'] * len(display_lst)

# display the chosen word hidden behind '_'
print(''.join(answer_list))
# print(word)

# learn condition for and/or
while hangman_ctr > 0 and right_guess < len(display_lst):
    is_right = False
    user_guess = input("Guess a letter: ").lower()
    if user_guess in answer_list:
        print(f"You have already guessed the letter: {user_guess}")
    else:
        for i in range(0, len(display_lst)):
            if user_guess == display_lst[i]:
                answer_list[i] = user_guess
                right_guess += 1
                is_right = True
        if  is_right == True:
            print(''.join(answer_list))
            print(hangman_art.hangman_life[full_life - hangman_ctr])
        else:
            print(f"Your guess {user_guess}, that's not in the word. You lose a life.")
            print(''.join(answer_list))
            hangman_ctr -= 1
            print(hangman_art.hangman_life[full_life - hangman_ctr])

if hangman_ctr == 0:
    print("Sorry but you lost, try again!")
    print(word)
else:
    print("Congratulations, you won!")

# join function works
# a = ['a', 'b', 'c']
# new_str = ''.join(a)
# print(new_str)

# str.replace works
# a = '____aa'
# #print(a.replace('_', 'b'))
# a = a.replace("_", "b", 1)
# print(a)
# a = a.replace("_", "1", 3)
# print(a)
# This does not work  a[1] = a[1].replace("_", "a")

# if "_" not in answer_lst: -> this code works if there is no more '_' in the answer_lst

# # filling '_' in a list
# # I forgot =+, so whenever I was adding '_' it was replacing the existing '_'
# display = []
# for _ in range(5):
#     display += '_'