from datetime import datetime, timedelta

def convert_iso8601_to_datetime(s : str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")

def fix_timezone_offset(t : datetime) -> datetime:
    """
        For some wacky reason, RadioJar decided to provide a weird tz offset with iso8601 formatting
        so we need to subtract 2 hours from every single timestamp...
    """
    return t - timedelta(hours=1)

def i_hate_radiojar(s : str) -> datetime:
    """A combination of the ISO8601 conversion and fix_tz_offset function"""
    return fix_timezone_offset(
        convert_iso8601_to_datetime(
            s
        )
    )

__all__ = [
    convert_iso8601_to_datetime,
    fix_timezone_offset,
    i_hate_radiojar
]