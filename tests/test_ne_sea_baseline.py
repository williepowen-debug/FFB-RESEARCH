"""Regression for conversion tries incorrectly entering ordinary NE/SEA offense."""
import importlib.util
from pathlib import Path
import unittest


path = Path(__file__).resolve().parents[1] / 'weekly/2026/week-01/research/ne-sea/compute_baseline.py'
spec = importlib.util.spec_from_file_location('ne_sea_baseline', path)
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


class ConversionAccountingTests(unittest.TestCase):
    def test_finite_epa_conversion_is_not_an_ordinary_target(self):
        # Relevant fields from Stevenson's successful 2025 NE-at-BAL conversion.
        # Finite EPA and an assigned receiver previously let this count as target 38.
        conversion = dict(play_type='pass', epa='1.053', two_point_attempt='1',
                          qb_kneel='0', qb_spike='0', play_deleted='0',
                          receiver_player_name='R.Stevenson')
        ordinary = dict(conversion, two_point_attempt='0')
        self.assertIsNotNone(baseline.number(conversion, 'epa'))
        self.assertTrue(baseline.eligible(ordinary))
        self.assertFalse(baseline.eligible(conversion))


if __name__ == '__main__':
    unittest.main()
