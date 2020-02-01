# -*- coding: utf-8 -*-

import jieba
import logging
import os
import pygtrie

path = os.path.abspath(os.path.dirname(__file__))

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
		with open(os.path.join(path, 'dict', d + '.txt')) as f:
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

class Converter:
	def __init__(this, from_region='cn', to_region='tw', no_phrases=False, fast=False):
		this.fast = fast

		if from_region == 't':
			this.TRIE_FROM = None
		else:
			this.TRIE_FROM = build_trie(choose_dicts(from_region, no_phrases, is_from=True))

		if to_region == 't':
			this.TRIE_TO = None
		else:
			this.TRIE_TO = build_trie(choose_dicts(to_region, no_phrases, is_from=False))

	def convert(this, s):
		if this.TRIE_FROM:
			s = replace_words(s, this.TRIE_FROM, fast=this.fast)
		if this.TRIE_TO:
			s = replace_words(s, this.TRIE_TO, fast=this.fast)
		return s
