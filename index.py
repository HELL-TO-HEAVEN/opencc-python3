#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import opencc2
import sys

parser = argparse.ArgumentParser(description='Open Chinese Convert (OpenCC) Command Line Tool')
parser.add_argument('-f', dest='from', default='cn', help='Default to cn (mainland China)')
parser.add_argument('-t', dest='to', default='tw', help='Default to tw (Taiwan)')
parser.add_argument('-i', dest='input', default=sys.stdin, type=argparse.FileType('r'), help='Input file (default to STDIN)')
parser.add_argument('-o', dest='output', default=sys.stdout, type=argparse.FileType('w'), help='Output file (default to STDOUT)')
parser.add_argument('-n', '--no-phrases', action='store_true', help='Convert without phrases')
parser.add_argument('-a', '--fast', action='store_true', help='Fast conversion (less accurate)')
args = parser.parse_args()

cc = opencc2.Converter(from_region=vars(args)['from'], to_region=vars(args)['to'], no_phrases=args.no_phrases, fast=args.fast)
args.output.write(cc.convert(args.input.read()))
