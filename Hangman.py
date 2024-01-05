import random

with open("words.txt", "r") as f:
    text = f.read()

words = text.split()
word_count = len(words)

word = words[random.randint(0, word_count - 1)]
# word = 'onomatopoeia'
num_guesses = 10

hidden_word = '_' * len(word)

guess = 1
garbage_letters = []
while guess <= num_guesses and '_' in hidden_word:
    if guess > 1:
        print(f'Ruled-out letters: {garbage_letters}')
    print(hidden_word)
    user_input = input(f'Enter a character (guess #{guess}): ')

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position + 1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[
                                                                position + 1:]  # Rebuild the hidden word string
        if user_input not in word:
            garbage_letters.append(user_input)

        guess += 1

if '_' in hidden_word:
    print('Loser!', end=' ')
else:
    print('Winner!', end=' ')

print(f'The word was {word}.')
