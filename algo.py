import os
import sys
import time
import data
import random

def border(a):
  for i in range(a):
    print('─', end = '')
  else:
    print('')
  
def title(a, b):
  border(b)
  print(a.center(b))
  border(b)

def notif(a, b, c):
  print('')

  txt = '» '
  txt = txt + a
  txt = txt + ' «'

  print(txt.center(b))

  time.sleep(c)

def clear(a):
  if a == 'all':
    os.system('cls')
  else:
    for i in range(a):
      sys.stdout.write('\033[F')
      for j in range(50):
        print(' ', end = '')
      else:
        print(end = '\r')

def wait(a):
  time.sleep(a)
  
def loading(a, b):
  print('')

  for i in range(b+1):  
    txt = '  » ' + a + '.' * i
    print (txt, end = '\r')
    time.sleep(1)

  os.system('cls')

def getWord(lists):
  if lists == 'animals':
    word =  random.choice(data.animals).upper()
  elif lists == 'countries':
    word = random.choice(data.countries).upper()
  
  for i in range(len(word)):
    if ' ' in word[i]:
      data.blank.append(' ')
      continue
    data.blank.append('ˍ')

  return word

def wrongGuess():
  if data.tries == 5:
    data.man[0] = '    O  '
  elif data.tries == 4:
    data.man[1] = '    |  '
    data.man[2] = '    |  '
  elif data.tries == 3:
    data.man[1] = '   \|  '
  elif data.tries == 2:
    data.man[1] = '   \|/ '
  elif data.tries == 1:
    data.man[3] = '   /   '
  elif data.tries == 0:
    data.man[3] = '   / \ '