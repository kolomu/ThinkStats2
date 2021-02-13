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
import nsfg


def MakeFrames():
    """Reads pregnancy data and partitions first babies and others.

    returns: DataFrames (all live births, first babies, others)
    """
    preg = nsfg.ReadFemPreg()

    # important to only inspect data where outcome = 1!
    live = preg[preg.outcome == 1]
    firsts = live[live.birthord == 1]
    others = live[live.birthord != 1]

    assert len(live) == 9148
    assert len(firsts) == 4413
    assert len(others) == 4735

    return live, firsts, others

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

""" Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. 
Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference 
in pregnancy length?
"""
def WeightDifference(live, firsts, others):
    # calculate mean for difference in lbs
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    print('Difference in lbs', mean1 - mean2) # firsts are lighter than others
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

    print('Cohen d', d) 
    return d


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

    live, firsts, others = first.MakeFrames()
    WeightDifference(live, firsts, others)


# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
if __name__ == '__main__':
    main(*sys.argv)
