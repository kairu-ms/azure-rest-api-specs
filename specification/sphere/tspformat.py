import json
import pathlib

# iterate over all the json files in tsp-output folder
path = pathlib.Path('./')
for file in path.rglob('tsp-output/**/*.json'):
    print(f"Reformat {file}")
    with open(file, 'r') as f:
        content = json.load(f)
    with open(file, 'w') as f:
        json.dump(content, f, indent=2, ensure_ascii=False, sort_keys=True)
