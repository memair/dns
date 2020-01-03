#!/usr/bin/python3

from datetime import datetime, timedelta, date
from update import state_should_change, SALT

start_date  = datetime(2020,1,1).date()
days = 366
state_change_count = 0

for i in range(days):
  date         = start_date + timedelta(i)
  change_state = state_should_change(date, SALT)

  if change_state:
    state_change_count += 1

  allow_social = state_change_count % 2 == 0

  print(f'{date} - {"unblocked" if allow_social else "blocked"}')