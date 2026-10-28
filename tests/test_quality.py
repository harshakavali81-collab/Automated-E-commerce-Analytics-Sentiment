import unittest
from src.processing.clean import clean_prices,clean_reviews
GOOD=dict(product_id="P1",product_name="Demo",category="Home",seller="Test",observed_date="2026-01-01",price="10",list_price="15",inventory="5",units_sold="3")
class QualityTests(unittest.TestCase):
 def test_reject_bad_data(self):
    records=[GOOD,{**GOOD,"price":"NaN","observed_date":"2026-01-02"},
      {**GOOD,"inventory":"-1","observed_date":"2026-01-03"},
      {**GOOD,"observed_date":"2026-02-31"}]
    a,q=clean_prices(records)
    self.assertEqual(len(a),1)
    self.assertEqual(q["rejected"],3)
 def test_report_duplicates(self):
    a,q=clean_prices([GOOD,{**GOOD,"price":"20"}])
    self.assertEqual(a[0][5],20)
    self.assertEqual(q["duplicates"],1)
 def test_invalid_reviews(self):
    rs=[dict(review_id="1",product_id="P1",review_date="2026-01-01",rating="5",review_text="Nice"),
      dict(review_id="2",product_id="unknown",review_date="2026-01-01",rating="1",review_text="Bad"),
      dict(review_id="3",product_id="P1",review_date="2026-01-01",rating="7",review_text="Good")]
    clean,q=clean_reviews(rs,{"P1"})
    self.assertEqual(len(clean),1)
    self.assertEqual(q["rejected"],2)
