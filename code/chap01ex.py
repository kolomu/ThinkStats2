"""
In the repository you downloaded, you should find a file named chap01ex.py; 
using this file as a starting place, write a function that reads the respondent file, 
2002FemResp.dat.gz.
The variable pregnum is a recode that indicates how many times each respondent has been pregnant. 
Print the value counts for this variable and compare them to the published results in the NSFG codebook.

You can also cross-validate the respondent and pregnancy files by comparing pregnum 
for each respondent with the number of records in the pregnancy file.

You can use nsfg.MakePregMap to make a dictionary that maps from each caseid to a list 
of indices into the pregnancy DataFrame.

A solution to this exercise is in chap01soln.py
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def validatePregnum(resp):
    # cross validate by numbers or records in preg file
    resp = nsfg.ReadFemResp()

    # caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(nsfg.ReadFemPreg())

    # iterate through the respondend pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from respondent file equals
        # number of records in preg file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main():
    resp = nsfg.ReadFemResp()
    pregnum = resp['pregnum'].value_counts().sort_index()
    print(pregnum)
    # cross validate by numbers or records in preg file
    print(validatePregnum(resp))


if __name__ == '__main__':
    main()
