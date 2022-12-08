#!/usr/bin/env python
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateplot import util
from functools import partial


def plot(infile, fmt, resolution, outfile):
    raw_input = infile.read().splitlines()
    rawstrings = pd.Series(raw_input)
    worker = partial(util.xform, fmt=fmt)
    dateobjs = rawstrings.apply(worker).sort_values()

    bins = util.bins(dateobjs.iloc[0], dateobjs.iloc[-1], resolution)

    fig, ax = plt.subplots(1, 1, figsize=(11, 8.5))
    ax.hist(dateobjs, color='lightblue', bins=bins)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
    if outfile:
        plt.savefig(outfile.buffer)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=argparse.FileType(), default=sys.stdin,
                        nargs='?')
    parser.add_argument("outfile", type=argparse.FileType(),
                        default=sys.stdout, nargs="?")
    parser.add_argument("-f", "--format", type=str,
                        default=util.WAYBACK_FORMAT)
    parser.add_argument("-r", "--resolution", type=str,
                        choices=["weeks", "days", "years", "months", "hours"],
                        default="weeks")
    arg = parser.parse_args()

    plot(arg.infile, arg.format, arg.resolution, arg.outfile)


if __name__ == "__main__":
    cli()
