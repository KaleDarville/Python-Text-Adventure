import time, os, sys

def typingPrint(text):
  words = text
  for char in words:
    time.sleep(0.06)
    sys.stdout.write(char)
    sys.stdout.flush()

def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.06)
  value = input()  
  return value

def clearScreen():
  os.system("clear")