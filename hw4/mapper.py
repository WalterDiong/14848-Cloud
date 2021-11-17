#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    dateInformation = int(line[15:23])
    temperature = int(line[87:92])
    quality = int(line[92])

    if (abs(temperature) == 9999 or not (quality == 0 or quality == 1 or quality == 4
        or quality == 5 or quality == 9)):
        continue

    print ('%s\t%s' % (dateInformation, temperature))
        
        
