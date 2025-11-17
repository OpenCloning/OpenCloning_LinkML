# OpenCloning_LinkML

A LinkML data model for [OpenCloning](https://opencloning.org/), a standardized schema for describing molecular cloning strategies and DNA assembly protocols.

## Website

You can access the model documentation at https://opencloning.github.io/OpenCloning_LinkML

## Migration from previous versions of the schema

If you have json files in older formats, you can migrate them to the latest version using the migrate command:

```bash
python -m opencloning_linkml.migrations.migrate file.json
```

This will create a new file with the same name but with the suffix `_backup.json` with the original data, and overwrite the original file with the migrated data.

You can also specify a target version to migrate to:

```bash
python -m opencloning_linkml.migrations.migrate file.json --target-version 0.2.9
```

And you can skip the backup (simply edit in place):

```bash
python -m opencloning_linkml.migrations.migrate file.json --no-backup
```

## Developer Documentation

The python package can be installed from PyPI:

```bash
pip install opencloning-linkml
```

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

### Creating a migration

To add a migration from version `X.Y.Z` to a new version `A.B.C`, follow these steps:

1. **Archive the current model**: Save a copy of the current Pydantic model to `src/opencloning_linkml/migrations/model_archive/vA_B_C.py`. This file should contain the complete model classes for version `A.B.C` (typically copied from `src/opencloning_linkml/datamodel/_models.py` after generating the new version).

2. **Create the transformation file**: Create a new file `src/opencloning_linkml/migrations/transformations/vX_Y_Z_to_vA_B_C.py` with a migration function

3. **Register the migration**: Add the migration to `src/opencloning_linkml/migrations/__init__.py`:
   - Import the migration function: `from .transformations.vX_Y_Z_to_vA_B_C import migrate_X_Y_Z_to_A_B_C`
   - Add it to the `load_migrations()` return dictionary: `("X.Y.Z", "A.B.C"): migrate_X_Y_Z_to_A_B_C`

4. **Add a test**: Add a test to `tests/test_migration.py` to ensure the migration works as expected.

**Example**: See `v0_2_8_to_v0_2_9.py` for a simple transformation example, or `v0_2_9_to_v_0_4_0.py` for a more complex migration with ID remapping and structural changes.


## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
