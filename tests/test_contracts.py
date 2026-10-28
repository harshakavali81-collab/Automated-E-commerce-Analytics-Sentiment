import csv
import tempfile
import unittest
from pathlib import Path
from src.ingestion.load_csv import read_csv
from src.processing.export import safe_cell,write_safe_csv

class ContractsTests(unittest.TestCase):
 def test_required_header_missing(self):
    with tempfile.TemporaryDirectory() as folder:
      path=Path(folder)/"x.csv";path.write_text("a,b\n1,2\n")
      with self.assertRaisesRegex(ValueError,"Missing required"):
        read_csv(path,required_columns=("a","missing"))
 def test_duplicate_column_rejected(self):
    with tempfile.TemporaryDirectory() as folder:
      path=Path(folder)/"x.csv";path.write_text("a,a\n1,2\n")
      with self.assertRaisesRegex(ValueError,"duplicate"):
        read_csv(path)
 def test_extra_cells_rejected(self):
    with tempfile.TemporaryDirectory() as folder:
      path=Path(folder)/"x.csv";path.write_text("a,b\n1,2,3\n")
      with self.assertRaisesRegex(ValueError,"exceeds"):
        read_csv(path)
 def test_csv_formula_payload_escaped(self):
    values=["=1+2","+IMPORTXML('x','y')","-2+3","@SUM(A1:A2)","\t=2"," safe"]
    result=write_safe_csv([{"name":v} for v in values],["name"])
    rows=list(csv.DictReader(result.splitlines()))
    for index in range(5):
      self.assertTrue(rows[index]["name"].startswith("'"))
    self.assertEqual(rows[5]["name"]," safe")
 def test_safe_nontext_preserved(self):
    self.assertEqual(safe_cell(123),123)
    self.assertEqual(safe_cell("regular product"),"regular product")
