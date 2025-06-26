import opencloning_linkml.datamodel._models as models
import json


with open("old_dict.json", "r") as f:
    old_dict = json.load(f)

for s in old_dict["sources"]:
    models.CollectionSource.model_validate(s)
