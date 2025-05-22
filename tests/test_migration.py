import unittest
from opencloning_linkml.migrations.migrate import migrate
import glob
import os
import json

test_folder = os.path.dirname(__file__)


class TestMigration(unittest.TestCase):
    def test_0_2_6_1_to_0_2_8(self):
        from opencloning_linkml.migrations.model_archive.v0_2_6_1 import CloningStrategy as old_CloningStrategy
        from opencloning_linkml.migrations.model_archive.v0_2_8 import CloningStrategy as new_CloningStrategy

        for file in glob.glob(os.path.join(test_folder, "migration/v0.2.6.1/*.json")):
            with open(file, "r") as f:
                data = json.load(f)
            old_cloning_strategy = old_CloningStrategy(**data)
            migrated_data = migrate(data, "0.2.8")
            new_cloning_strategy = new_CloningStrategy(**migrated_data)

            old_dict = old_cloning_strategy.model_dump()
            new_dict = new_cloning_strategy.model_dump()

            # The only thing that changes is the addition of these fields
            old_dict["schema_version"] = "0.2.8"
            old_dict["backend_version"] = None
            old_dict["frontend_version"] = None

            self.assertEqual(old_dict, new_dict)
