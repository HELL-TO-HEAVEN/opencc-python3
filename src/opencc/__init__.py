# -*- coding: utf-8 -*-

from .opencc2 import Converter
from .version import __version__

def main():
	import argparse
	import sys

	parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
	parser.add_argument('-v', '--version', action='version', version='OpenCC 2 version ' + __version__)
	parser.add_argument('-f', '--from', default='cn', help='Type of variant of the original text. Default to Simplified Chinese (Mainland China) (represented by “cn”)')
	parser.add_argument('-t', '--to', default='tw', help='Type of variant of the target text. Default to Traditional Chinese (Taiwan) (represented by “tw”)')
	parser.add_argument('-i', dest='input', default=sys.stdin, type=argparse.FileType('r'), help='Path to the input file. Default to stdin')
	parser.add_argument('-o', dest='output', default=sys.stdout, type=argparse.FileType('w'), help='Path to the output file. Default to stdout')
	parser.add_argument('-n', '--no-phrases', action='store_true', help='Disable phrase conversion (e.g. convert 内存 to 記憶體)')
	args = parser.parse_args()

	cc = Converter(from_variant=vars(args)['from'], to_variant=vars(args)['to'], with_phrases=not args.no_phrases)
	args.output.write(cc.convert(args.input.read()))
