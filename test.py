from unittest import TestCase

from gamble import gamble_karma


class TestGamble(TestCase):
    def test_gamble_karma(self):
        results = [gamble_karma() for _ in xrange(250000)]
        expected_value = float(sum(results)) / len(results)
        self.assertLess(expected_value, 1)
