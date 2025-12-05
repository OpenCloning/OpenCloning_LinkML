"""Test validators."""

import unittest
from pydantic import ValidationError

from opencloning_linkml.datamodel import ManuallyTypedSequence


class TestValidation(unittest.TestCase):
    """Test validators."""

    # Test cases: (crick_overhang, watson_overhang, circular, should_raise_error)
    test_cases = [
        # Valid cases
        (0, 0, True, False),
        (0, 0, False, False),
        (2, 3, False, False),
        (None, None, False, False),
        # Invalid cases - circular with non-zero overhangs
        (2, 0, True, True),
        (0, 3, True, True),
        (2, 3, True, True),
        (0, 0, True, False),
        (0, None, True, False),
        (None, None, True, False),
    ]

    def test_circular_overhangs_validation(self):
        """Test that circular sequences must have zero overhangs."""
        for crick, watson, circular, should_raise in self.test_cases:
            print(crick, watson, circular, should_raise)

            kwargs = {
                "id": 1,
                "sequence": "ATCGATCG",
                "circular": circular,
            }
            if crick is not None:
                kwargs["overhang_crick_3prime"] = crick
            if watson is not None:
                kwargs["overhang_watson_3prime"] = watson

            if should_raise:
                with self.assertRaises(ValidationError):
                    ManuallyTypedSequence(**kwargs)
            else:
                ManuallyTypedSequence(**kwargs)
