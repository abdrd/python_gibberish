import string 
import random
import datetime
import time

def generate_random_str(length, chunks):
  chars = list(string.ascii_lowercase + string.ascii_uppercase +'0' + '1' + '2' + '3' + '4' + '5' + '6' + '7' + '8' + '9')

  result = ''
  for i in range(chunks):
    for i in range(length):
      picked = random.choice(chars)
      result += picked
    result += '\n'

  print('Generating gibberish...')
  time.sleep(2)

  exact_time = datetime.datetime.now()
  date = str(datetime.date(exact_time.year, exact_time.month, exact_time.day))
  hours = str(datetime.time(exact_time.hour, exact_time.minute, exact_time.second))
  now = date + '_' + hours
  
  fd = now.replace(':', '_')
  file_date = fd.replace('-', '_')
  
  f_handle = open(f'{result[:5]}_AT_{file_date}.txt', 'w+')

  f_handle.write(result)

  print(f'DONE! The file name is {result[:6]}_AT_{file_date}.txt')

chunks = int(input('How many chunks do you want in your .txt file? '))
length = int(input('How many characters do you want in one chunk? '))


generate_random_str(length, chunks)