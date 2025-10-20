import re

with open("src/opencloning_linkml/datamodel/_models.py", "r") as f:
    content = f.read()

new_content = []
change_next_line = False
for line in content.split("\n"):
    new_line = line
    if re.match(r"^\s+input:", line):
        change_next_line = True
    elif change_next_line:
        new_line = new_line.replace("default=None", "default_factory=list")
        change_next_line = False
    new_content.append(new_line)

with open("src/opencloning_linkml/datamodel/_models.py", "w") as f:
    f.write("\n".join(new_content))
