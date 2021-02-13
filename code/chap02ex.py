"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


# The mode of a distribution is the most frequent value.
def Mode(hist):
    """Returns the value with the highest frequency.
    hist: Hist object
    returns: value from Hist
    """
    # max is a python function which takes iterable and returns highest value
    # if it is dictionary it takes the key (frequency) as comparison value not the "value"!
    # we are not interested in frequency but the "value"
    frequency, value = max([(frequency, value) for value, frequency in hist.Items()]) 
    return value

def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.
    hist: Hist object
    returns: iterator of value-freq pairs
    """
    # itemgetter docu: https://docs.python.org/3/howto/sorting.html
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)


# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
if __name__ == '__main__':
    main(*sys.argv)
