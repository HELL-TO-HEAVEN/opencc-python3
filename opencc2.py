#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import jieba
import logging
import os
import pygtrie
import sys

jieba.setLogLevel(logging.INFO)

def choose_dicts(region, no_phrases, is_from=True):
	if is_from:  # dict from
		if region == 'cn':
			return ('STCharacters', 'STPhrases')
		if region == 'sg':
			if no_phrases:
				return ('STCharacters', 'STPhrases')
			else:
				raise NotImplementedError('sg phrases is currently not supported, consider adding --no-phrases')
		if region == 'hk':
			if no_phrases:
				return ('HKVariantsRev', 'HKVariantsRevPhrases')
			else:
				raise NotImplementedError('hk phrases is currently not supported, consider adding --no-phrases')
		if region == 'tw':
			if no_phrases:
				return ('TWVariantsRev', 'TWVariantsRevPhrases')
			else:
				return ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
		if region == 'jp':
			if no_phrases:
				return ('JPVariantsRev',)
			else:
				raise NotImplementedError('jp phrases is currently not supported, consider adding --no-phrases')
	else:
		if region == 'cn':
			return ('TSCharacters', 'TSPhrases')
		if region == 'sg':
			if no_phrases:
				return ('TSCharacters', 'TSPhrases')
			else:
				raise NotImplementedError('sg phrases is currently not supported, consider adding --no-phrases')
		if region == 'hk':
			if no_phrases:
				return ('HKVariants', 'HKVariantsPhrases')
			else:
				raise NotImplementedError('hk phrases is currently not supported, consider adding --no-phrases')
		if region == 'tw':
			if no_phrases:
				return ('TWVariants',)
			else:
				return ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
		if region == 'jp':
			if no_phrases:
				return ('JPVariants',)
			else:
				raise NotImplementedError('jp phrases is currently not supported, consider adding --no-phrases')
	raise Exception('Unrecognized region: ' + region)

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
		for i in t:
			jieba.add_word(i)
		l = []
		for word in jieba.cut(s):
			l.append(replace_words_plain(word, t))
		return ''.join(l)

parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
parser.add_argument('-f', dest='from', default='cn', help='Default to cn (mainland China)')
parser.add_argument('-t', dest='to', default='tw', help='Default to tw (Taiwan)')
parser.add_argument('-i', dest='input', help='Input file (default to STDIN)')
parser.add_argument('-o', dest='output', help='Output file (default to STDOUT)')
parser.add_argument('-n', '--no-phrases', action='store_true', help='Convert without phrases')
parser.add_argument('-a', '--fast', action='store_true', help='Fast conversion (less accurate)')
args = parser.parse_args()

if not args.input:
	s = sys.stdin.read()
else:
	with open(args.input) as f:
		s = f.read()

if vars(args)['from'] != 't':
	s = replace_words(s, build_trie(choose_dicts(vars(args)['from'], args.no_phrases, is_from=True)), fast=args.fast)
if args.to != 't':
	s = replace_words(s, build_trie(choose_dicts(args.to, args.no_phrases, is_from=False)), fast=args.fast)

if not args.output:
	sys.stdout.write(s)
else:
	with open(args.output, 'w') as f:
		f.write(s)
