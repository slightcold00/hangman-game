import random
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle fox frog goat goose hawk lion lizard monkey moose mouse mule owl panda parrot rabbit ram rat python spider seal snake raven tiger turkey turtle wolf zebra'.split()

def randomword(wordlist):
     wordIndex = random.randint(0,len(wordlist)-1)
     return wordlist[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretwords):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()
    
    blanks = '_'*len(secretwords)

    for i in range(len(secretwords)):#replay blank with correctly guessed letters
        if secretwords[i] in correctLetters:
          blanks = blanks[:i] + secretwords[i] + blanks[i+1:]

    for letter in blanks:
      print(letter,end=' ')
    print()

def getGuess(alreadyGuess):
  while True:
    print('Guess a letter.(The word is a kind of animal)')
    guess = input()
    guess = guess.lower()
    if len(guess) !=1:
      print('Please enter a single letter.')
    elif guess in alreadyGuess:
      print('You have already guessed that letter.Choose again.')
    elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
      print('Please enter a LETTER')
    else:
      return guess

def playAgain():
  print('Do you want to play again?(yes or no)')
  return input().lower().startswith('y'or'Y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretwords = randomword(words)
gameIsDone = False

while True:
  displayBoard(HANGMANPICS,missedLetters,correctLetters,secretwords)

  guess = getGuess(missedLetters+correctLetters)

  if guess in secretwords:
       correctLetters = correctLetters+guess

       foundAllLetters = True
       for i in range(len(secretwords)):
         if secretwords[i] not in correctLetters:
           foundAllLetters = False
           break
       if foundAllLetters:
         displayBoard(HANGMANPICS,missedLetters,correctLetters,secretwords)
         print('Yes! The secret word is "'+secretwords+'"! You have won!')
         gameIsDone = True
  else:
    missedLetters = missedLetters + guess
    if len(missedLetters) == len(HANGMANPICS) - 1:
      displayBoard(HANGMANPICS,missedLetters,correctLetters,secretwords)
      print('You have run out of guesses!\nAfter '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses, the word was "'+secretwords+'"')
      gameIsDone=True

  if gameIsDone:
   if playAgain():
     missedLetters=''
     correctLetters=''
     gameIsDone=False
     secretwords=randomword(words)
   else:
     break

