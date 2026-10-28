"""Load authorized CSV sources, never scrape retail sites."""
import csv
from pathlib import Path
def read_csv(path):
    path=Path(path)
    if not path.is_file():raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig",newline="") as fp:
        reader=csv.DictReader(fp)
        if not reader.fieldnames:raise ValueError("Missing CSV header")
        return list(reader)
