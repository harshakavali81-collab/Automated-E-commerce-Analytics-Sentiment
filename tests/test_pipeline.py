import unittest,tempfile,sqlite3
from pathlib import Path
from src.pipeline.run import execute
from src.ingestion.generate_demo import generate
from src.analytics.metrics import daily
class PipelineTests(unittest.TestCase):
 def test_deterministic(self):
    with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
        self.assertEqual(generate(a,days=15),generate(b,days=15))
        self.assertEqual((Path(a)/"prices.csv").read_bytes(),(Path(b)/"prices.csv").read_bytes())
 def test_end_to_end_idempotent(self):
    with tempfile.TemporaryDirectory() as root:
        root=Path(root);source=root/"raw";out=root/"out"
        generate(source,days=8)
        a=execute(source/"prices.csv",source/"reviews.csv",out)
        b=execute(source/"prices.csv",source/"reviews.csv",out)
        self.assertEqual(a["observation_count"],96)
        self.assertEqual(a["estimated_revenue"],b["estimated_revenue"])
        with sqlite3.connect(out/"commerce.sqlite") as conn:self.assertEqual(len(daily(conn)),8)
 def test_demo_mode(self):
    with tempfile.TemporaryDirectory() as root:
        root=Path(root)
        result=execute(root/"raw/prices.csv",root/"raw/reviews.csv",root/"out",demo=True)
        self.assertEqual(result["observation_count"],1440)
        self.assertEqual(result["product_count"],12)
        self.assertEqual(result["source_kind"],"synthetic_demo")
 def test_missing_files(self):
    with tempfile.TemporaryDirectory() as root:
        with self.assertRaises(FileNotFoundError):
            execute(Path(root)/"none.csv",Path(root)/"reviews.csv",Path(root)/"out")
