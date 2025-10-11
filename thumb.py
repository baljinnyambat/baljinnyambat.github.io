import os
from PIL import Image


def get_folder_names(directory_path):
    folder_names = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            folder_names.append(entry)
    return folder_names


def generate_small(folder, TARGET_WIDTH=500):
    INPUT_DIR = "project/" + folder
    OUTPUT_DIR = "small/" + folder
    print(f"Starting thumbnail generation (Output format: JPEG)...")

    try:
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            print(f"Created output directory: {OUTPUT_DIR}")
    except OSError as e:
        print(f"Error creating directory {OUTPUT_DIR}: {e}")
        return

    files_processed = 0

    try:
        for filename in os.listdir(INPUT_DIR):
            if filename.lower().endswith((".png")):

                input_path = os.path.join(INPUT_DIR, filename)

                base_name, _ = os.path.splitext(filename)
                output_filename = f"{base_name}.jpg"
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                try:
                    img = Image.open(input_path)

                    img = img.convert("RGB")
                    width, height = img.size

                    new_height = int(height * (TARGET_WIDTH / width))

                    img = img.resize((TARGET_WIDTH, new_height))

                    img.save(output_path, "JPEG", quality=98, optimize=True)

                    print(f"Successfully created JPEG thumbnail for: {filename}")
                    files_processed += 1

                except Exception as e:
                    print(f"--- ERROR processing {filename}: {e}")

    except FileNotFoundError:
        print(f"\nFATAL ERROR: The input directory '{INPUT_DIR}' was not found.")
        print("Please create this folder and place your PNG files inside it.")
        return

    print("\n--- Thumbnail Generation Complete ---")
    print(f"Total files processed: {files_processed}")


alldir = get_folder_names("project")
for dir in alldir:
    generate_small(dir)
