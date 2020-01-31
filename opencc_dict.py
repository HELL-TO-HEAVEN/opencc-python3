#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import pickle
import pygtrie

def makedict(ds):  # build a trie
    t = pygtrie.CharTrie()
    for d in ds:  # read a list of dictionaries
        with open(os.path.join('dict', d + '.txt')) as f:
            for line in f:
                if line != '\n' and line[0] != '#':  # ignore empty and commented lines
                    l, r = line.rstrip().split('\t')  # split the line by TAB
                    t[l] = r  # put words into the trie
    return t

def write_dicts():
    for k, v in DICT_FROM.items():
        t = makedict(v)
        with open('data/' + k + '2t.pickle', 'wb') as f:
            pickle.dump(t, f)

    for k, v in DICT_TO.items():
        t = makedict(v)
        with open('data/t2' + k + '.pickle', 'wb') as f:
            pickle.dump(t, f)

#write_dicts()

parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool - Dictionary')
parser.add_argument('-t', '--to', choices=('txt', 'pickle'), required=True, help='to dictionary format')
parser.add_argument('-s', '--source', action='append', required=True, help='source file path')
parser.add_argument('-d', '--dest', required=True, help='destination file path')
args = parser.parse_args()
print(args)
