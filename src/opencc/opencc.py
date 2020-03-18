# -*- coding: utf-8 -*-

import os
import pygtrie
import sys

# Dictionary

DICT_FROM = \
	{ 'cn': ('STCharacters', 'STPhrases')
	, 'sg': ('STCharacters', 'STPhrases')
	, 'hk': ('HKVariantsRev', 'HKVariantsRevPhrases')
	, 'twp': ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
	, 'tw': ('TWVariantsRev', 'TWVariantsRevPhrases')
	, 'jp': ('JPVariantsRev',)
	}

DICT_TO = \
	{ 'cn': ('TSCharacters', 'TSPhrases')
	, 'sg': ('TSCharacters', 'TSPhrases')
	, 'hk': ('HKVariants', 'HKVariantsPhrases')
	, 'twp': ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
	, 'tw': ('TWVariants',)
	, 'jp': ('JPVariants',)
	}

def choose_dict_from(variant):
	try:
		return DICT_FROM[variant]
	except KeyError:
		print('Error: Variant name', variant, 'does not exists.')
		sys.exit(0)

def choose_dict_to(variant):
	try:
		return DICT_TO[variant]
	except KeyError:
		print('Error: Variant name', variant, 'does not exists.')
		sys.exit(0)

# Trie

def build_trie(ds):  # build a trie
	path = os.path.abspath(os.path.dirname(__file__))
	t = pygtrie.CharTrie()
	for d in ds:  # read a list of dictionaries
		with open(os.path.join(path, 'data/data', d + '.txt')) as f:
			for line in f:
				if line != '\n' and line[0] != '#':  # ignore empty and commented lines
					l, r = line.rstrip().split('\t')  # split the line by TAB
					t[l] = r  # put words into the trie
	return t

# Replace

def replace_words_plain(s, t):
	l = []  # list of converted words
	while s:
		longest_prefix = t.longest_prefix(s)  # match the longest prefix
		if not longest_prefix:  # if the prefix does not exist
			l.append(s[0])  # append the first character
			s = s[1:]  # remove the first character from the string
		else:  # if exists
			l.append(longest_prefix.value.split(' ')[0])  # append the first converted word
			s = s[len(longest_prefix.key):]  # remove the word from the string
	return ''.join(l)

def replace_words(s, t):
	return replace_words_plain(s, t)
	'''else:
		for i in t:
			jieba.add_word(i)
		l = []
		for word in jieba.cut(s):
			l.append(replace_words_plain(word, t))
		return ''.join(l)'''

# Class

class Converter:
	def __init__(this, from_variant='cn', to_variant='tw'):
		if from_variant == 't':
			this.TRIE_FROM = None
		else:
			this.TRIE_FROM = build_trie(choose_dict_from(from_variant))

		if to_variant == 't':
			this.TRIE_TO = None
		else:
			this.TRIE_TO = build_trie(choose_dict_to(to_variant))

	def convert(this, s):
		if this.TRIE_FROM:
			s = replace_words(s, this.TRIE_FROM)
		if this.TRIE_TO:
			s = replace_words(s, this.TRIE_TO)
		return s
