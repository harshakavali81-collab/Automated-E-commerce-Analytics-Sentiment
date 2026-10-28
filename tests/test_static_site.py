import json
import tempfile
import unittest
from pathlib import Path
from scripts.build_site import build

class StaticSiteTests(unittest.TestCase):
 def test_synthetic_source_only(self):
    with tempfile.TemporaryDirectory() as folder:
      path=Path(folder)/"public"
      output=build(path)
      self.assertEqual(output["charts"],10)
      self.assertEqual(output["records"],1440)
      self.assertEqual(set(output["files"]),{"index.html","metrics.json","robots.txt",".nojekyll"})
      self.assertEqual((path/"index.html").read_text().count('class="panel chart"'),10)
      self.assertFalse((path/"_fixture").exists())
      self.assertNotIn("Excellent quality, fast delivery, love it",(path/"index.html").read_text())
      self.assertEqual(json.loads((path/"metrics.json").read_text())["source_kind"],"synthetic_demo")
 def test_refuse_repository_root(self):
    with self.assertRaises(ValueError):
      build(".")
