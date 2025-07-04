import unittest
from opencloning_linkml.migrations import migrate
from opencloning_linkml.migrations.migrate import main as migrate_script_main
import glob
import os
import json
import tempfile
import shutil
from unittest.mock import patch

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

    def test_0_2_8_to_0_2_9(self):
        from opencloning_linkml.migrations.model_archive.v0_2_8 import (
            CloningStrategy as old_CloningStrategy,
            GibsonAssemblySource,
            UploadedFileSource,
        )
        from opencloning_linkml.migrations.model_archive.v0_2_9 import CloningStrategy as new_CloningStrategy

        # Test example files
        for file in glob.glob(os.path.join(test_folder, "migration/v0.2.6.1/*.json")):
            with open(file, "r") as f:
                data = json.load(f)

            old_CloningStrategy(**data)
            migrated_data = migrate(data, "0.2.9")
            # Sufficient that it can parse the data
            new_CloningStrategy(**migrated_data)

            # If we try again, we get none
            self.assertIsNone(migrate(migrated_data, "0.2.9"))

        # Test particular example
        # Test that the coordinates are converted correctly
        s1 = GibsonAssemblySource.model_validate(
            {
                "id": 1,
                "input": [2],
                "output": 3,
                "circular": False,
                "assembly": [
                    {
                        "left_location": {"start": 0, "end": 100, "strand": None},
                        # Inter-base location
                        "right_location": {"start": 0, "end": 0, "strand": None},
                        "sequence": 3,
                        "reverse_complemented": False,
                    }
                ],
            }
        )
        s2 = UploadedFileSource.model_validate(
            {
                "id": 2,
                "input": [],
                "output": 3,
                "coordinates": {"start": 0, "end": 100, "strand": None},
                "sequence_file_format": "fasta",
                "file_name": "test.fasta",
                "index_in_file": 0,
                "circularize": False,
            }
        )

        data = {
            "sources": [s1.model_dump(), s2.model_dump()],
            "sequences": [],
            "primers": [],
        }

        migrated_data = migrate(data, "0.2.9")
        cs = new_CloningStrategy(**migrated_data)
        self.assertEqual(cs.sources[0].assembly[0].left_location, "1..100")
        self.assertEqual(cs.sources[0].assembly[0].right_location, "0^1")
        self.assertEqual(cs.sources[1].coordinates, "1..100")

    def test_0_2_9_to_0_4_0(self):
        from opencloning_linkml.migrations.model_archive.v0_2_9 import CloningStrategy as old_CloningStrategy
        from opencloning_linkml.migrations.model_archive.v0_4_0 import CloningStrategy as new_CloningStrategy

        for file in glob.glob(os.path.join(test_folder, "migration/v0.2.9/*.json")):
            with open(file, "r") as f:
                data = json.load(f)

            old_CloningStrategy(**data)
            migrated_data = migrate(data, "0.4.0")
            new_cloning_strategy = new_CloningStrategy(**migrated_data)

            source_ids = [source.id for source in new_cloning_strategy.sources]
            sequence_ids = [sequence.id for sequence in new_cloning_strategy.sequences]
            self.assertEqual(source_ids, sequence_ids)
            self.assertEqual(source_ids, list(range(1, len(source_ids) + 1)))

            # Check that the file ids have been remapped
            if "files" in file:
                for file in migrated_data["files"]:
                    self.assertEqual(file["sequence_id"], 1)

    def test_migration_script(self):

        with tempfile.TemporaryDirectory() as tmp_dir:
            example_file = os.path.join(test_folder, "migration/v0.2.6.1/homologous_recombination.json")
            test_file = os.path.join(tmp_dir, "homologous_recombination.json")
            backup_file = test_file.replace(".json", "_backup.json")
            shutil.copy(example_file, test_file)

            with patch("builtins.print") as mock_print:
                migrate_script_main(test_file, backup=True, target_version="0.4.0")
                mock_print.assert_any_call(f"Original file backed up as {test_file.replace('.json', '_backup.json')}")
                mock_print.assert_any_call(f"Migrated {test_file} to version 0.4.0")

            with open(test_file, "r") as f:
                data = json.load(f)
            self.assertEqual(data["schema_version"], "0.4.0")
            self.assertEqual(data["backend_version"], None)
            self.assertEqual(data["frontend_version"], None)

            # By default, it will backup the original file
            self.assertTrue(os.path.exists(backup_file))

            # A backup file cannot be used as input
            with patch("builtins.print") as mock_print:
                migrate_script_main(backup_file, backup=False, target_version=None)
                mock_print.assert_any_call(f"Skipping {backup_file} because it is a backup file")

            # Clear directory
            for file in os.listdir(tmp_dir):
                os.remove(os.path.join(tmp_dir, file))
            shutil.copy(example_file, test_file)

            # Test that it works with a target version and no backup
            migrate_script_main(test_file, backup=False, target_version="0.2.8")

            with open(test_file, "r") as f:
                data = json.load(f)
            self.assertEqual(data["schema_version"], "0.2.8")
            self.assertFalse(os.path.exists(backup_file))

            # Test that the migration is not done if the target version is the same as the current version
            with patch("builtins.print") as mock_print:
                migrate_script_main(test_file, backup=False, target_version="0.2.8")
                mock_print.assert_any_call(f"No migration needed for {test_file}")

            with open(test_file, "r") as f:
                data = json.load(f)
            self.assertEqual(data["schema_version"], "0.2.8")
            self.assertEqual(data["backend_version"], None)
            self.assertEqual(data["frontend_version"], None)

            # Can migrate from 0.2.8 to 0.2.9
            migrate_script_main(test_file, backup=False, target_version="0.2.9")

            with open(test_file, "r") as f:
                data = json.load(f)
            self.assertEqual(data["schema_version"], "0.2.9")
            self.assertEqual(data["backend_version"], None)
            self.assertEqual(data["frontend_version"], None)
