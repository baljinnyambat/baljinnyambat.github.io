import os
import json


def get_folder_names(directory_path):
    folder_names = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            folder_names.append(entry)
    return folder_names


def get_file_names(directory_path):
    file_names = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            file_names.append(entry)
    return file_names


data = {"projects": []}

filename = "output.json"
folders = get_folder_names("project")

for folder in folders:
    files = get_file_names("project/" + folder)
    images = []
    for file in files:
        images.append(file)

    entity = {
        "folder": folder,
        "name": folder,
        "type": "Branding",
        "cover": images[0] if images else "",
        "images": images,
    }

    data["projects"].append(entity)

# Open the file in write mode ('w') and use json.dump()
with open(filename, "w") as f:
    json.dump(data, f, indent=4)
