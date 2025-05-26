from .__init__ import migrate

import os
import json
import shutil


def main(input_file: str, backup, target_version):
    if input_file.endswith("backup.json"):
        print(f"Skipping {input_file} because it is a backup file")
        return

    with open(input_file, "r") as f:
        data = json.load(f)

    migrated_data = migrate(data, target_version)
    if migrated_data is None:
        print(f"No migration needed for {input_file}")
        return

    # Create a backup of the original file
    if backup:
        name, extension = os.path.splitext(input_file)
        input_file_old = name + "_backup" + extension
        shutil.copy2(input_file, input_file_old)
        print(f"Original file backed up as {input_file_old}")

    # Write migrated data back to the same file
    with open(input_file, "w") as f:
        json.dump(migrated_data, f, indent=2)

    print(f"Migrated {input_file} to version {migrated_data['schema_version']}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Migrate JSON files to a target schema version.")
    parser.add_argument("input_files", nargs="+", help="Input JSON files to migrate")
    parser.add_argument("--target-version", default=None, help="Target schema version (optional)")
    parser.add_argument("--no-backup", default=False, help="Do not backup the original file", action="store_true")

    args = parser.parse_args()

    for input_file in args.input_files:

        main(input_file, not args.no_backup, args.target_version)
