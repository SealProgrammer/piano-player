from pyautogui import *
from time import sleep
PAUSE = 0.01
delay = 0.02
sleep(2)

with open('song.txt', 'r') as f:

  song = f.read().replace('\n',' ').split()

for note in song:
  if note.startswith('[') and note.endswith(']'):
    hotkey(*note[1:-1])
    sleep(0.02)
  else:
    if not note.startswith('-'):
      write(note)
      sleep(delay)
    else:
      sleep(delay * (len(str(note))+1))