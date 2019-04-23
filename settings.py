from datetime import date

from stringLibs import rpad

def init():
  global high_pole 
  global low_pole
  global logging
  global logfile

  high_pole = "lazers"
  low_pole = "feelings"
  logging = True

  today = date.today()
  logfile = f'game-{rpad(today.year,2,"0")}.{rpad(today.month,2,"0")}.{rpad(today.day,2,"0")}.log'


