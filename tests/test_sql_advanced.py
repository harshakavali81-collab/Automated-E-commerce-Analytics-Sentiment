"""Smoke-test every advanced SQL case against the documented snapshot schema."""
import sqlite3,tempfile,unittest
from pathlib import Path
from src.ingestion.generate_demo import generate
from src.pipeline.run import execute

class AdvancedSQLTests(unittest.TestCase):
 def test_advanced_queries_execute_and_return_rows(self):
    with tempfile.TemporaryDirectory() as temp:
      root=Path(temp);generate(root/"raw",days=10)
      execute(root/"raw/prices.csv",root/"raw/reviews.csv",root/"processed")
      sql=Path("sql/advanced_analytics.sql").read_text(encoding="utf-8")
      statements=[s.strip() for s in sql.split(";") if s.strip()]
      self.assertEqual(len(statements),5)
      with sqlite3.connect(root/"processed/commerce.sqlite") as con:
        for query in statements:
          with self.subTest(query=query[:70]):
            data=con.execute(query).fetchall()
            self.assertGreater(len(data),0)
