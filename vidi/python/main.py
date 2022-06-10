#!/usr/bin/python3

# Objective of exercise
# 1. Take a Markdown file as input (file or stdin)
# 2. Convert output to HTML (either to designated output, or stdout)

import argparse
from sys import stdin, stdout
from typing import TextIO
import markdown


class Converter:
    def __init__(self, *, input: TextIO, output: TextIO, is_stdin: bool):
        self.input = input
        self.output = output
        self.is_stdin = is_stdin

    def run(self):
        if self.is_stdin:
            line = self.input.readline()
            while line:
                self.process(line)
                self.output.flush()  # immediately flush, otherwise stdout can't receive anything
                line = self.input.readline()
        else:
            for line in self.input.readlines():
                self.process(line)
            self.output.flush()

    def process(self, line: str):
        out = markdown.markdown(line)
        self.output.write(out)

    def close(self):
        self.input.close()
        self.output.close()


def main():
    args = parse_args()
    is_stdin = args.get('in') is None
    input = stdin if is_stdin else open(args['in'], 'r')
    output = stdout if args.get('out') is None else open(args['out'], 'w')
    conv = Converter(input=input, output=output, is_stdin=is_stdin)
    conv.run()
    conv.close()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--out', help='Output to this file, default to stdout.')
    parser.add_argument('-i', '--in', help='Input file, default to stdin.')
    return vars(parser.parse_args())


if __name__ == '__main__':
    main()
