# -*- coding: utf-8 -*-

from .opencc import Converter
from .version import __version__

def main():
	import argparse
	import sys

	parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool (Python 3 Implementation)')
	parser.add_argument('-v', '--version', action='version', version='OpenCC (Python 3 Implementation) version ' + __version__)
	parser.add_argument('-f', '--from', default='cn', help='Type of variant of the original text. Default to Simplified Chinese (Mainland China) (represented by “cn”)')
	parser.add_argument('-t', '--to', default='twp', help='Type of variant of the target text. Default to Traditional Chinese (Taiwan) (with phrases) (represented by “twp”)')
	parser.add_argument('-i', dest='input', help='Path to the input file. Default to stdin')
	parser.add_argument('-o', dest='output', help='Path to the output file. Default to stdout')
	args = parser.parse_args()

	cc = Converter(from_variant=vars(args)['from'], to_variant=vars(args)['to'])
	if args.input:
		with open(args.input) as f:
			s = f.read()
	else:
		s = sys.stdin.read()
	s = cc.convert(s)
	if args.output:
		with open(args.output) as f:
			f.write(s)
	else:
		sys.stdout.write(s)
