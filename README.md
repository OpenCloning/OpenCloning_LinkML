# OpenCloning_LinkML

A LinkML data model for OpenCloning, a standardized schema for describing molecular cloning strategies and DNA assembly protocols.

## Website

https://opencloning.github.io/OpenCloning_LinkML

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [opencloning_linkml](src/opencloning_linkml)
    * [schema](src/opencloning_linkml/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/opencloning_linkml/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

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
