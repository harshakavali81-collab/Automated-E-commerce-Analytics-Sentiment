"""Read locally authorized CSV with explicit header validation.

No scraping and no remote URL ingestion. Input rows are validated separately.
"""
import csv
from pathlib import Path

def read_csv(path, required_columns=None):
    path=Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig",newline="") as fp:
        reader=csv.DictReader(fp)
        columns=reader.fieldnames
        if not columns:
            raise ValueError("Missing CSV header: "+str(path))
        if len(set(columns))!=len(columns) or any(not c or c.strip()!=c for c in columns):
            raise ValueError("Invalid/duplicate CSV column names: "+str(path))
        if required_columns:
            missing=sorted(set(required_columns)-set(columns))
            if missing:
                raise ValueError("Missing required columns in "+str(path)+": "+", ".join(missing))
        rows=list(reader)
        # csv.DictReader places extra unheaded fields under key None.
        if any(None in row for row in rows):
            raise ValueError("CSV row exceeds declared column count: "+str(path))
        return rows
