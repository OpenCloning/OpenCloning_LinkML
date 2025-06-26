"""Data test."""

import os
import glob
import unittest

from linkml_runtime.loaders import json_loader
from opencloning_linkml.datamodel import CloningStrategy

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "data")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, "**/*.json"), recursive=True)

known_exceptions = ["submission.json", "pcr_based_targeting.json"]

EXAMPLE_FILES = [f for f in EXAMPLE_FILES if os.path.basename(f) not in known_exceptions]


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            try:
                obj = json_loader.load(path, target_class=CloningStrategy)
                assert obj
            except Exception:
                raise AssertionError(f"Error loading \033[93m{path}\033[0m")
