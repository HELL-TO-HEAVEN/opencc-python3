from .opencc2 import Converter
from .version import __version__

def main():
	import argparse
	import sys

	parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
	parser.add_argument('-f', '--from', default='cn', help='Type of original text. Default to Simplified Chinese (Mainland China) (represented by “cn”)')
	parser.add_argument('-t', '--to', default='tw', help='Type of target text. Default to Traditional Chinese (Taiwan) (represented by “tw”)')
	parser.add_argument('-i', dest='input', default=sys.stdin, type=argparse.FileType('r'), help='Path to the input file. Default to stdin')
	parser.add_argument('-o', dest='output', default=sys.stdout, type=argparse.FileType('w'), help='Path to the output file. Default to stdout')
	parser.add_argument('-n', '--no-phrases', action='store_true', help='Disable phrase conversion (e.g. convert 内存 to 記憶體)')
	parser.add_argument('-a', '--fast', action='store_true', help='Enable fast conversion (with lower accuracy)')
	args = parser.parse_args()

	cc = Converter(from_region=vars(args)['from'], to_region=vars(args)['to'], with_phrases=not args.no_phrases, fast=args.fast)
	args.output.write(cc.convert(args.input.read()))
