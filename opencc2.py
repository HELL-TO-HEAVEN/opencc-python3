#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import jieba
import os
import pygtrie
import sys

def choose_dicts(region, no_phrases, is_from_region=True):
    if is_from_region:  # dict from
        if region == 'cn':
            return ('STCharacters', 'STPhrases')
        if region == 'hk':
            if no_phrases:
                return ('HKVariantsRev', 'HKVariantsRevPhrases')
            else:
                raise NotImplementedError('Cannot convert hk with phrases')
        if region == 'tw':
            if no_phrases:
                return ('TWVariantsRev', 'TWVariantsRevPhrases')
            else:
                return ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
        if region == 'jp':
            if no_phrases:
                return ('JPVariantsRev',)
            else:
                raise NotImplementedError('從日本詞彙轉換是無效的')
    else:
        if region == 'cn':
            return ('TSCharacters', 'TSPhrases')
        if region == 'hk':
            if no_phrases:
                return ('HKVariants', 'HKVariantsPhrases')
            else:
                raise NotImplementedError('Cannot convert hk with phrases')
        if region == 'tw':
            if no_phrases:
                return ('TWVariants',)
            else:
                return ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
        if region == 'jp':
            if no_phrases:
                return ('JPVariants',)
            else:
                raise NotImplementedError('從日本詞彙轉換是無效的')

def build_trie(ds):  # build a trie
    t = pygtrie.CharTrie()
    for d in ds:  # read a list of dictionaries
        with open(os.path.join('dict', d + '.txt')) as f:
            for line in f:
                if line != '\n' and line[0] != '#':  # ignore empty and commented lines
                    l, r = line.rstrip().split('\t')  # split the line by TAB
                    t[l] = r  # put words into the trie
    return t

def replace_words_plain(s, t):
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

def replace_words(s, t, fast=False):
    if fast:
        return replace_words_plain(s, t)
    else:
        l = []
        for word in jieba.cut(s):
            l.append(replace_words_plain(word, t))
        return ''.join(l)

parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
parser.add_argument('-f', '--from', default='cn', dest='from_region', help='from region')
parser.add_argument('-t', '--to', default='tw', dest='to_region', help='to region')
parser.add_argument('-i', '--input', help='input')
parser.add_argument('-o', '--output', help='output')
parser.add_argument('--no-phrases', action='store_true', help='Convert without phrases')
parser.add_argument('--fast', action='store_true', help='Fast conversion')
args = parser.parse_args()

print(args)

if not args.input:
    s = sys.stdin.read()
else:
    with open(args.input) as f:
        s = f.read()

if args.from_region != 't':
    s = replace_words(s, build_trie(choose_dicts(args.from_region, args.no_phrases, is_from_region=True)), fast=args.fast)
if args.to_region != 't':
    s = replace_words(s, build_trie(choose_dicts(args.to_region, args.no_phrases, is_from_region=False)), fast=args.fast)

if not args.output:
    sys.stdout.write(s)
else:
    with open(args.output, 'w') as f:
        f.write(s)
