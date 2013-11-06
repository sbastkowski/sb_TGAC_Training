#! /usr/bin/env python
import sqer
import argparse
import screed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='+')

    args = parser.parse_args()

    total = 0
    for filename in args.filenames:
	print 'Counting totals'
        records = screed.open(filename)
        total += sqer.sum_bp_records(records)

    print '%d bp total' % total

if __name__ == '__main__':
    main()
