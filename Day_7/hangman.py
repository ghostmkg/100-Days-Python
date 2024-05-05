import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)   #prinint Logo

print("Welcome to hangman game.")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']   #ASCI for hangman life

word_list = [
    "Wolverine", "Spider Man", "Thor", "Iron Man", "Hulk", "Captain America", "Daredevil",
    "Punisher", "Deadpool", "Silver Surfer", "Gambit", "Cyclops", "Mr Fantastic",
    "Nightcrawler", "Nick Fury", "Human Torch", "Iceman", "Professor X",  "Colossus",
    "Bucky Barnes", "Doctor Strange", "Storm", "Jean Grey","Rogue","Elektra", "Emma Frost",
    "Thing", "Black Bolt", "She Hulk", "Invisible Woman", "Namor" "Black Panther", "Beast",
    "Kitty Pryde", "Sentry", "Hawkeye", "Luke Cage", "Iron Fist", "Scarlet Witch", "Cable",
    "Hercules", "Hank Pym", "Moon Knight", "Angel", "Betsy Braddock", "War Machine",
    "Carol Danvers", "Black Cat", "Captain Marvel", "Warpath", "Madrox", "Quicksilver",
    "Spider Woman", "Domino", "Vision", "Black Widow", "Blade", "Speedball", "Wonder Man",
    "Beta Ray Bill", "Sam Wilson", "Captain Britain", "Songbird", "Quasar", "Shang Chi",
    "Strong Guy", "Havok", "Rick Jones", "Amadeus Cho", "Cloak", "Adam Warlock", 
    "Molly Hayes", "Jessica Jones", "Krrish", "Bat Man", "Super Man", "Aquaman", "Joker"
]   #word list for guessing

lives = 6

chosen_word =  random.choice(word_list).lower()

word_len = len(chosen_word)

display = []

# Displaying _ at place of every letter

for i in chosen_word:
    if i == " ":
        display.append(" ")
    else:
        display.append("_")

print(display)
end_of_game = False

# Running the loop till the you lose or win

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checking the user input is a letter or word and if user is repeating the word.
    if len(guess) > 1:
        print("You have enter more then a letter.")
        continue
    elif guess in display:
        print("You have already guess the letter. Please enter new letter")
        print(display)
        continue
    for letter in range(0,word_len):    #replacing _ with correct guess letter
        if guess == chosen_word[letter]:
            display[letter] = guess
    if guess not in chosen_word:    #decreasing live for every wrong guesses
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
        
    print(' '.join(display))   
    if "_" not in display:   #Termenting the game when user won or lose.
        end_of_game = True
        print("You Won!")
    print(stages[lives])