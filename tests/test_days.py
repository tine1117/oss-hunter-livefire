import unittest
from duration_utils import parse_duration
class ParseDurationDays(unittest.TestCase):
  def test_days(self):
    self.assertEqual(parse_duration("1d"), 86400)
