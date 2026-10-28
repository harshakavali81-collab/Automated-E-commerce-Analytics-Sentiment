import csv
import sqlite3
import tempfile
import unittest
from pathlib import Path
from src.analytics.alerts import build_alerts
from src.analytics.report import render_report
from src.ingestion.generate_demo import generate
from src.pipeline.run import execute

class AdvancedTests(unittest.TestCase):
 def test_thresholds_rejected(self):
    with sqlite3.connect(":memory:") as con:
      with self.assertRaises(ValueError):build_alerts(con,change_threshold=0)
      with self.assertRaises(ValueError):build_alerts(con,stock_threshold=-1)
 def test_reject_nan_and_noninteger_thresholds(self):
    with sqlite3.connect(":memory:") as con:
      with self.assertRaises(ValueError):build_alerts(con,change_threshold=float("nan"))
      with self.assertRaises(ValueError):build_alerts(con,change_threshold=float("inf"))
      with self.assertRaises(ValueError):build_alerts(con,stock_threshold=2.5)
      with self.assertRaises(ValueError):build_alerts(con,stock_threshold=True)
 def test_explainable_price_change_alert(self):
    with sqlite3.connect(":memory:") as con:
      con.execute("CREATE TABLE prices(product_id TEXT,product_name TEXT,observed_date TEXT,price REAL,inventory INTEGER)")
      con.executemany("INSERT INTO prices VALUES(?,?,?,?,?)",[
        ("A","Demo","2026-01-01",100,30),("A","Demo","2026-01-02",140,5),
        ("B","Example","2026-01-01",90,20)])
      a=build_alerts(con,change_threshold=20)
      self.assertEqual(a["price_movement_count"],1)
      self.assertEqual(a["low_stock_count"],1)
      self.assertEqual(a["price_movements"][0]["change_pct"],40.0)
 def test_ten_source_charts(self):
    with tempfile.TemporaryDirectory() as base:
      base=Path(base);generate(base/"raw",days=12)
      execute(base/"raw/prices.csv",base/"raw/reviews.csv",base/"out")
      report=base/"report.html"
      value=render_report(base/"out/commerce.sqlite",report)
      self.assertEqual(value["charts"],10)
      self.assertEqual(report.read_text().count('class="panel chart"'),10)
 def test_html_escape_for_untrusted_product_name(self):
    with tempfile.TemporaryDirectory() as base:
      base=Path(base);generate(base/"raw",days=1);path=base/"raw/prices.csv"
      with path.open(newline="",encoding="utf-8") as fp:
        reader=csv.DictReader(fp);columns=reader.fieldnames;rows=list(reader)
      rows[0]["product_name"]="<script>alert(1)</script>"
      with path.open("w",newline="",encoding="utf-8") as fp:
        writer=csv.DictWriter(fp,fieldnames=columns);writer.writeheader();writer.writerows(rows)
      out=base/"out";execute(path,base/"raw/reviews.csv",out)
      report=base/"report.html";render_report(out/"commerce.sqlite",report)
      html=report.read_text(encoding="utf-8")
      self.assertNotIn("<script>alert(1)</script>",html)
      self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;",html)
