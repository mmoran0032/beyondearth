#!/usr/bin/env python3


import fnmatch
import os
import re
import subprocess

filetag = '>((\d|\w|/|_|\s|\(|\)|-)+\.\w+)<'
tagpattern = re.compile(filetag)
fileattr = 'file="((\d|\w|/|_|\s|\(|\)|-)+\.\w+)"'
attrpattern = re.compile(fileattr)


def main():
    files = [f for f in os.listdir('.') if fnmatch.fnmatch(f, '*.modinfo')]
    print('Processing: {}'.format(files))
    for filename in files:
        subprocess.call(['cp', filename, '{}-original'.format(filename)])
        with open(filename, 'rU') as f:
            contents = [line.rstrip() for line in f]
        write_to_file(filename, contents)


def write_to_file(filename, contents):
    with open(filename, 'w') as f:
        for line in contents:
            line = process_pattern(line, tagpattern)
            line = process_pattern(line, attrpattern)
            f.write('{}\n'.format(line))


def process_pattern(line, pattern):
    matches = re.findall(pattern, line)
    if matches:
        line = reformat_line(line, matches)
    return line


def reformat_line(line, matches):
    print('   {}'.format(line))
    to_change = matches[0][0]
    line = line.replace(to_change, to_change.lower())
    print('>> {}'.format(line))
    return line


if __name__ == '__main__':
    main()
