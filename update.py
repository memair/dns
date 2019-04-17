#!/usr/bin/python3

import hashlib, os
from datetime import datetime, timedelta, date

def state_should_change(date, salt):
  """pseudorandomly returns true on 25% of dates"""

  salted_date_string = (date.strftime('%Y-%m-%d') + salt).encode('utf-8')
  salted_date_hex = hashlib.md5(salted_date_string).hexdigest()
  return int(salted_date_hex[-1], 16) % 4 == 0

salt = 'dns.memair.com'
start_date  = datetime(2019,1,1).date()
today = datetime.now().date()
state_change_count = 0

delta = today - start_date

for i in range(delta.days + 1):
  date         = start_date + timedelta(i)
  change_state = state_should_change(date, salt)

  if change_state:
    state_change_count += 1

allow_social = state_change_count % 2 == 0

print(f'{today} - {"unblocked" if allow_social else "blocked"}')

if allow_social:
  print('allowing social media today')
  os.system("sed -i '/memair/s/^#*/#/g' /etc/pihole/adlists.list")
else:
  print('blocking social media today')
  os.system("sed -i '/memair/s/^#*//g' /etc/pihole/adlists.list")

print('refreshing pihole lists')
os.system("pihole -g")
