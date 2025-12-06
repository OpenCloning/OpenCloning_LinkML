rm -f src/data/templates/*/templates/*backup.json
python -m opencloning_linkml.migrations.migrate --target-version 0.4.9 src/data/templates/*/templates/*.json
rm -f src/data/templates/*/templates/*backup.json
