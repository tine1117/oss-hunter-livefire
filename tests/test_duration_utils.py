 class TestParseDuration(unittest.TestCase):
     # ... existing tests ...
+
+    def test_days(self):
+        self.assertEqual(parse_duration("1d"), 86400)
+        self.assertEqual(parse_duration("2d4h"), 2*86400 + 4*3600)
+        self.assertEqual(parse_duration("0d"), 0)
+        self.assertEqual(parse_duration("1d30m"), 86400 + 1800)