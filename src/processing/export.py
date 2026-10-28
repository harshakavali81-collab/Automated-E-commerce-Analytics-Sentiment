"""Escape spreadsheet formula injection in user-supplied textual CSV exports."""
import csv
import io

DANGEROUS_PREFIXES=("=","+","-","@","\t","\r","\n")

def safe_cell(value):
    if isinstance(value,str) and value.lstrip(" ").startswith(DANGEROUS_PREFIXES):
        # Prefix text with a literal apostrophe to stop Excel/Sheets evaluation.
        return "'"+value
    return value

def write_safe_csv(records,columns):
    stream=io.StringIO(newline="")
    writer=csv.DictWriter(stream,fieldnames=columns,extrasaction="ignore")
    writer.writeheader()
    for item in records:
        writer.writerow({k:safe_cell(item.get(k,"")) for k in columns})
    return stream.getvalue()
