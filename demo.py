#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import pygtrie
import sys

def build_trie(ds):  # build a trie
    t = pygtrie.CharTrie()
    for d in ds:  # read a list of dictionaries
        with open(os.path.join('dict', d + '.txt')) as f:
            for line in f:
                if line != '\n' and line[0] != '#':  # ignore empty and commented lines
                    l, r = line.rstrip().split('\t')  # split the line by TAB
                    t[l] = r  # put words into the trie
    return t

def replace_words(s, t):
    l = []  # list of coverted words
    while s:
        longest_prefix = t.longest_prefix(s)  # match the longest prefix
        if not longest_prefix:  # if the prefix does not exist
            l.append(s[0])  # append the first character
            s = s[1:]  # remove the first character from the string
        else:  # if exists
            l.append(longest_prefix.value.split(' ')[0])  # append the first converted word
            s = s[len(longest_prefix.key):]  # remove the word from the string
    return ''.join(l)

DICT_FROM = \
    { 'cn': ('STCharacters', 'STPhrases')
    , 'hk': ('HKVariantsRev', 'HKVariantsRevPhrases')
    , 'tw': ('TWVariantsRev', 'TWVariantsRevPhrases')
    , 'twp': ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
    , 'jp': ('JPVariantsRev',)
    }

DICT_TO = \
    { 'cn': ('TSCharacters', 'TSPhrases')
    , 'hk': ('HKVariants', 'HKVariantsPhrases')
    , 'tw': ('TWVariants',)
    , 'twp': ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
    , 'jp': ('JPVariants',)
    }

parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
parser.add_argument('-f', '--from', default='cn', dest='from_region', help='from region')
parser.add_argument('-t', '--to', default='twp', dest='to_region', help='to region')
args = parser.parse_args()

s = sys.stdin.read()
if args.from_region != 't':
    s = replace_words(s, build_trie(DICT_FROM[args.from_region]))
if args.to_region != 't':
    s = replace_words(s, build_trie(DICT_TO[args.to_region]))
sys.stdout.write(s)
