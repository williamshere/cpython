import unittest
from test import support
from unittest import mock

with mock.patch('webbrowser.open'):
    import antigravity

class AntigravityTests(unittest.TestCase):
    def test_geohash(self):
        with support.captured_stdout() as captured_output:
            antigravity.geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
        self.assertEqual(captured_output.getvalue(), '37.857713 -122.544543\n')

if __name__ == "__main__":
    unittest.main()
