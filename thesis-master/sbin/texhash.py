#!/usr/bin/env python2

__author__ = "Joshua Steffensky <joshua.steffensky@cispa.saarland>"

import os
import argparse
import hashlib

BLOCKSIZE = 65536

def calchash(flist):
    hash = hashlib.sha512()
    for f in flist:
        with open(f, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hash.update(buf)
                buf = afile.read(BLOCKSIZE)
    return hash.hexdigest()


def checkending(filename, endings):
    for e in endings:
        if filename.endswith(e):
            return True

def discoverfilesrecursive(dir, endings):
    flist = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            if checkending(f, endings):
                flist.append(os.path.join(root, f))
    return flist

def discoverfilesnonrecursive(dir, endings):
    flist = []
    root, dirs, files = os.walk(dir).next()
    for f in files:
        if checkending(f, endings):
            flist.append(os.path.join(root, f))
    return flist

def discoverfiles(recursive, dir, endings):
    if recursive:
        return discoverfilesrecursive(dir, endings)
    else:
        return discoverfilesnonrecursive(dir, endings)

def _parse_args():
    parser = argparse.ArgumentParser(
        description="Calculates a hash for (multifile) latex document")
    parser.add_argument("--recursive", action='store_true', help="walk directories recursively")
    parser.add_argument("--dir", type=str, default=".", help="start directory")
    parser.add_argument("ENDING", type=str, help="endings to regard", nargs='+')
    return parser.parse_args(), parser


def main():
    c_args, parser = _parse_args()
    flist = discoverfiles(c_args.recursive, c_args.dir, c_args.ENDING)
    print calchash(flist)


if __name__ == "__main__":
    main()
