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

    priority_order = ["hours", "days", "weeks", "months", "years", "years"]
    label_resolution_dict = {
        "years": mdates.YearLocator,
        "days": mdates.DayLocator,
        "weeks": mdates.MonthLocator,
        "months": mdates.MonthLocator,
        "hours": mdates.HourLocator
    }
    tick_res = priority_order[priority_order.index(resolution)]
    label_ticks = util.bins(dateobjs.iloc[0], dateobjs.iloc[-1], tick_res)
    while label_ticks > 50:
        tick_res = priority_order[priority_order.index(resolution) + 1]
        label_ticks = util.bins(dateobjs.iloc[0], dateobjs.iloc[-1], tick_res)

    bins = util.bins(dateobjs.iloc[0], dateobjs.iloc[-1], resolution)

    fig, ax = plt.subplots(1, 1, figsize=(11, 8.5))
    ax.hist(dateobjs, color='#990000', bins=bins)
    ax.xaxis.set_major_locator(label_resolution_dict[tick_res]())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
    plt.xticks(rotation=45)
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
