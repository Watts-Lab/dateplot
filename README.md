# DatePlot

This is a tool that will quickly create a temporal density plot from a list of dates. By default it takes the wayback format, but an arbitrary `date`-like format can be used.

# Installation

```
pip install git+https://github.com/Watts-Lab/dateplot.git
```

# Sample Usage

This uses imagemagick's display feature. You can also redirect the output to a png file and view that however you want by replacing `| display` with `> plot.png`. 

```
dateplot < test_dates.txt | display
```

## Resolution

You can select your preferred resolution with the `-r` flag. Supported choices are weeks, days, years, months, and hours.

```
dateplot -r weeks < test_dates.txt | display
```

## format

Since this was built for use with the News Observatory, the default format is `%Y%m%d%H%M%S` which isn't very common in other contexts. 
You can specify any `date`-like format with the `-f` flag.
Imagine we have a csv where the 3rd column is a date in the format `%Y-%m-%d`.

```
awk -F, '(NR>1) {print $3}' data.csv | dateplot -f "%Y-%m-%d"| display
```
