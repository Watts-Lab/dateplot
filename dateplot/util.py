from datetime import datetime
import re
from dateutil import rrule

WAYBACK_FORMAT = '%Y%m%d%H%M%S'


def date_extract(s, comp: re.Pattern):
    match_obj = comp.search(s)
    if match_obj:
        return match_obj.group(0)
    else:
        return None


def xform(s, fmt=WAYBACK_FORMAT):
    # This feels kinda hacky but it might work?
    today = datetime.now()
    datestring = today.strftime(fmt)
    dateformat_pattern = re.sub(r"\d", r"\\d", datestring)
    extracted_string = date_extract(s, re.compile(dateformat_pattern))
    if extracted_string:
        return datetime.strptime(extracted_string, fmt)
    else:
        print(f"datestring {s} does not appear to contain a date in "
              f"format {fmt}, please check your input data, "
              f"this datestring will be dropped!")
        return None


def bins(start: datetime, end: datetime, resolution: str):
    assert resolution in {"years", "days", "months", "weeks", "hours"}
    rrule_str = resolution[:-1].upper() + "LY"
    interval = getattr(rrule, rrule_str)
    corr_delta = len(list(rrule.rrule(interval, dtstart=start, until=end)))
    return corr_delta
