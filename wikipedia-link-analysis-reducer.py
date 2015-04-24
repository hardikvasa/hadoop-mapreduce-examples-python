#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None


for line in sys.stdin:    # input comes from STDIN
    line = line.strip()    # remove leading and trailing whitespace

    word, count = line.split('\t', 1)    # parse the input we got from mapper.py by a tab (space)

    try:    
        count = int(count)     # convert count from string to int
    except ValueError:
        continue        #If the count is not a number then discard the line by doing nothing


    if current_word == word:      #comparing the current word with the previous word (since they are ordered by key (word))
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

if current_word == word:    # do not forget to output the last word if needed!
    print '%s\t%s' % (current_word, current_count)
