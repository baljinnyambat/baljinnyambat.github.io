import tinify
import os

# tinify.key = "yvqKgBhFM2bDwkdGMFnblVLHff0p80Bf" Magsar 200rem
# MzYgzjyTwKCN4Bj0shrJl4dFz2nqYKyc
tinify.key = "MzYgzjyTwKCN4Bj0shrJl4dFz2nqYKyc"

project1 = [
    "hybr",
    "luc",
    "baruun",
    "ezegt",
    "bats",
    "misheel",
    "insur",
    "mid",
    "ded",
    "nsug",
    "travida",
    "dayan",
    "bank",
    "ubcab",
    "4ex",
    "urnha",
    "circus",
    "score",
    "west",
    "jet",
    "indra",
    "mgns",
    "silk",
    "shira",
    "thermo",
    "villa",
    "esm",
    "lera",
    "indrrr",
    "binary",
    "redc",
    "uvid",
    "buynt",
    "farm",
    "serial",
    "mass",
    "terra",
    "otgoo",
    "brich",
    "als",
    "hera20",
    "oims",
    "arc",
    "1min",
    "dav",
    "medimpex",
    "cty",
]

project2 = [
    "jump",
    "market",
    "ind",
    "ns",
    "zep",
    "green",
    "shaman",
    "winter",
    "ic",
    "tumursukh",
    "alpha",
    "zorig",
    "ogoomor",
]


def compress_folder(proj):
    INPUT_DIR = "rem/" + proj
    OUTPUT_DIR = "comp/" + proj

    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        # Check if the file is a supported image type (optional, but good practice)
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            try:
                print(f"Compressing: {filename}...")
                source = tinify.from_file(input_path)
                source.to_file(output_path)
                print(f"Compressed and saved to: {output_path}")

            except tinify.errors.TinifyAPIException as err:
                print(f"API Error for {filename}: {err.message}")
            except Exception as e:
                print(f"An unexpected error occurred for {filename}: {e}")
        else:
            print(f"Skipping non-image file: {filename}")


def get_folder_names(directory_path):
    """
    Returns a list of folder names within the specified directory.
    """
    folder_names = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            folder_names.append(entry)
    return folder_names


# Example usage:
for project in project2:
    compress_folder(project)
