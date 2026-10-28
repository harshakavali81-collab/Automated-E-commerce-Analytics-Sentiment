import unittest
from src.sentiment.lexicon import label,score
class SentimentTests(unittest.TestCase):
 def test_positive(self):self.assertEqual(label("Excellent and amazing"),"positive")
 def test_negative(self):self.assertEqual(label("Terrible, broken"),"negative")
 def test_neutral(self):self.assertEqual(label("Arrived Tuesday."),"neutral")
 def test_negated_positive(self):self.assertEqual(label("Not good"),"negative")
 def test_negated_negative(self):self.assertEqual(label("Not bad"),"positive")
 def test_case(self):self.assertEqual(label("LOVE it"),"positive")
 def test_inert_text(self):self.assertEqual(score("<script>alert(1)</script>"),0)
