import algo
import data
import display

def main():
  algo.clear('all')

  algo.title('HANGMAN', 50)
  print(' [1] Play')
  print(' [2] Exit')
  algo.border(50)
  
  menu = input(' Choose menu: ')

  if menu == '1':
    categories()
    return
  elif menu == '2':
    algo.loading('Exiting program', 3)
    return

def categories():
  algo.clear('all')

  algo.title('HANGMAN', 50)
  print(' [1] Animals')
  print(' [2] Countries')
  algo.border(50)

  ctg = input(' Choose category: ')

  if ctg == '1':
    ctg = 'animals'
  elif ctg == '2':
    ctg = 'countries'
  else:
    algo.notif('Wrong menu input !', 50, 1)
    categories()
    return

  word = algo.getWord(ctg)
  play(ctg, word)
  
def play(ctg, word):
  algo.clear('all')

  algo.title('HANGMAN: ' + ctg, 50)
  display.hangplay()

  print(' Word = ', end = '')
  for i in data.blank:
    print(i, end = '')
  else:
    print('')
  algo.border(50)

  win = False

  if win == True:
    text = '\'' + word + '\'' + ' is the word, YOU WIN !'
    algo.notif(text, 50, 1)
    backMenu()
    return

  if data.tries == 0:
    algo.notif('HANGMAN ! you failed guess the word', 50, 1)
    algo.notif(word + ' is the correct word', 50, 1)
    backMenu()
    return
  
  if 'ˍ' in data.blank:
    guess = input(' Guess a word / a letter: ').upper()

    if guess == '':
        algo.notif('Please enter alphabetical character', 50, 1)
        play(ctg, word)
        return

    elif len(guess) == 1:
      if not guess.isalpha():
        algo.notif('Please enter alphabetical character', 50, 1)
        play(ctg, word)
        return
      for i in data.guessedWord:
        if guess == i:
          algo.notif('You\'ve guess the letter before', 50, 1)
          play(ctg, word)
          return
      
      index = 0
      isExist = False
      for i in word:
        if guess == i:
          data.blank[index] = guess
          isExist = True
        else:
          data.guessedWord.append(guess)
        index += 1

      if isExist == False:
        data.tries -= 1
        algo.wrongGuess()

        text = '\'' + guess + '\'' + ' is not exist'
        algo.notif(text, 50, 1)
  
    elif len(guess) != 1 and guess != word:
      data.tries -= 1
      algo.wrongGuess()

      text = '\'' + guess + '\'' + ' is not the word'
      algo.notif(text, 50, 1)

    else:
      for i in range(len(word)):
        data.blank[i] = word[i]
      win = True

  else:
    text = '\'' + word + '\'' + ' is the word, YOU WIN !'
    algo.notif(text, 50, 1)
    backMenu()
    return

  play(ctg, word)

def backMenu():
  print('')
  algo.border(50)
  input(' Press enter to continue')
  data.reset()
  main()
  return

main()