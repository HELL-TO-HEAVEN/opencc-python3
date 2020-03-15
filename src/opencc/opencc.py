# -*- coding: utf-8 -*-

# import jieba
import logging
import os
import pygtrie

def choose_dicts(variant, with_phrases, is_from=True):
	if is_from:  # dict from
		if variant == 'cn':
			return ('STCharacters', 'STPhrases')
		if variant == 'sg':
			if with_phrases:
				raise NotImplementedError('sg phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('STCharacters', 'STPhrases')
		if variant == 'hk':
			if with_phrases:
				raise NotImplementedError('hk phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('HKVariantsRev', 'HKVariantsRevPhrases')
		if variant == 'tw':
			if with_phrases:
				return ('TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev')
			else:
				return ('TWVariantsRev', 'TWVariantsRevPhrases')
		if variant == 'jp':
			if with_phrases:
				raise NotImplementedError('jp phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('JPVariantsRev',)
	else:
		if variant == 'cn':
			return ('TSCharacters', 'TSPhrases')
		if variant == 'sg':
			if with_phrases:
				raise NotImplementedError('sg phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('TSCharacters', 'TSPhrases')
		if variant == 'hk':
			if with_phrases:
				raise NotImplementedError('hk phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('HKVariants', 'HKVariantsPhrases')
		if variant == 'tw':
			if with_phrases:
				return ('TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther')
			else:
				return ('TWVariants',)
		if variant == 'jp':
			if with_phrases:
				raise NotImplementedError('jp phrases is currently not supported, consider adding --no-phrases')
			else:
				return ('JPVariants',)
	raise Exception('Unrecognized variant: ' + variant)

def build_trie(ds):  # build a trie
	path = os.path.abspath(os.path.dirname(__file__))
	t = pygtrie.CharTrie()
	for d in ds:  # read a list of dictionaries
		with open(os.path.join(path, 'opencc2-dict/data', d + '.txt')) as f:
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

def replace_words(s, t):
	if True:
		return replace_words_plain(s, t)
	else:
		for i in t:
			jieba.add_word(i)
		l = []
		for word in jieba.cut(s):
			l.append(replace_words_plain(word, t))
		return ''.join(l)

class Converter:
	def __init__(this, from_variant='cn', to_variant='tw', with_phrases=True):
		this.fast = fast

		if from_variant == 't':
			this.TRIE_FROM = None
		else:
			this.TRIE_FROM = build_trie(choose_dicts(from_variant, with_phrases, is_from=True))

		if to_variant == 't':
			this.TRIE_TO = None
		else:
			this.TRIE_TO = build_trie(choose_dicts(to_variant, with_phrases, is_from=False))

	def convert(this, s):
		if this.TRIE_FROM:
			s = replace_words(s, this.TRIE_FROM)
		if this.TRIE_TO:
			s = replace_words(s, this.TRIE_TO)
		return s
