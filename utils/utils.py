from datetime import datetime
import re


def convert_date_range(date_str, year=2025):
    # Clean non-breaking spaces and weird dashes
    date_str = date_str.replace('\u2009', ' ').replace('\u2013', '-').replace('\u2014', '-')

    # Extract parts like: Apr 25 - 30
    match = re.match(r"([A-Za-z]+)\s+(\d+)\s*-\s*(\d+)", date_str)
    if not match:
        raise ValueError("Date format is invalid")

    month_str, start_day, end_day = match.groups()

    # Convert month name to number
    start_date = datetime.strptime(f"{start_day} {month_str} {year}", "%d %b %Y")
    end_date = datetime.strptime(f"{end_day} {month_str} {year}", "%d %b %Y")

    # Manually remove leading zeros and format as M/D/YYYY
    start_formatted = f"{start_date.month}/{start_date.day}/{start_date.year}"
    end_formatted = f"{end_date.month}/{end_date.day}/{end_date.year}"
    return f"{start_formatted} - {end_formatted}"

def normalize_price(price_str):
    # Remove currency symbol and commas
    clean = price_str.replace("₪", "").replace(",", "").replace("$", "")
    # Convert to float, then back to int if possible
    value = float(clean)
    return int(value)