from m5stack import *
from m5ui import *
from uiflow import *

import utime

state = {}
state['active'] = False
state['start'] = None
state['end'] = None

def lcd_print(text):
  setScreenColor(0x000000)
  lcd.print(text, 0, 5, 0xffffff)

def now():
  return int(utime.time())

def format_session(seconds):
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    if hours > 0:
        return str(hours) + 'h ' + str(minutes % 60) + 'm'
    if minutes > 0:
        return str(minutes) + 'm ' + str(seconds % 60) + 's'
    return str(seconds) + 's'

def trigger():
  global state

  state['active'] = not state['active']
  if state['active']:
    state['start'] = now()
    lcd_print('Clocking in')
  else:
    state['end'] = now()
    duration_in_seconds = int(state['end'] - state['start'])
    lcd_print('Clocking\nout\nafter:\n' + format_session(duration_in_seconds))

btnA.wasPressed(trigger)

lcd_print('Punchcard\nloaded!')

