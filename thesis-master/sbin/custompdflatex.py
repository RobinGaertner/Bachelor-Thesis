#!/usr/bin/env python

__author__ = "Joshua Steffensky <joshua.steffensky@cispa.saarland>"

import sys
import re
import subprocess


def main():
    split = sys.argv.index("--")
    todefine = sys.argv[1:split]
    args=sys.argv[split+1:len(sys.argv)]
    split = args.index("??")
    texfile = args[split+1:len(args)][0]
    args = args[0:split]

    preamble = ""
    for v in todefine:
        name, command = v.split("=")
        preamble += "\def\%s{%s}" % (name, command)
    
    preamble += "\input{%s}"% (texfile,)
    print preamble
    
    for i in range(0,3):
        pdflatex = subprocess.Popen(["pdflatex"] + args, stdin=subprocess.PIPE)
        stdout, stderr= pdflatex.communicate(input=preamble)

    print stdout
    print stderr



if __name__ == "__main__":
    main()
