#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_date = None
current_max_temp = None
  
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    date, temp = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        temp = int(temp)
        date = int(date)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_date is None:
        current_date = date
    if current_max_temp is None:
        current_max_temp = temp
    
    if current_date == date:
        if temp > current_max_temp:
            current_max_temp = temp
    else:
        if current_date:
            print ('%s\t%s' % (current_date, current_max_temp))
        current_date = date
        current_max_temp = temp

if current_date:
    print ('%s\t%s' % (current_date, current_max_temp))