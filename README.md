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

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
