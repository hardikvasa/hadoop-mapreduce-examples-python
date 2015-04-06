#!/usr/bin/env python

import sys

for line in sys.stdin:    # Input is read from STDIN and the output of this file is written into STDOUT
    line = line.strip()    # remove leading and trailing whitespace
    words = line.split()   # split the line into words
    
    for word in words:   
        print '%s\t%s' % (word, 1)   #Print all words (key) individually with the value 1
