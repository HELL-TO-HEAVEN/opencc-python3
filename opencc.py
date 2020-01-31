#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pickle
import pygtrie
import sys

def load_dict_from(region):
    with open('data/' + region + '2t.pickle', 'rb') as f:
        return pickle.load(f)

def load_dict_to(region):
    with open('data/t2' + region + '.pickle', 'rb') as f:
        return pickle.load(f)

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

parser = argparse.ArgumentParser(description='A simple implementation of OpenCC')
parser.add_argument('-f', '--from', default='cn', dest='from_region', help='from region')
parser.add_argument('-t', '--to', default='twp', dest='to_region', help='to region')
args = parser.parse_args()

s = sys.stdin.read()

if args.from_region != 't':
    s = replace_words(s, load_dict_from(args.from_region))

if args.to_region != 't':
    s = replace_words(s, load_dict_to(args.to_region))

sys.stdout.write(s)
