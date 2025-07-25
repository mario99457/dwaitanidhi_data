import os
import json

def process_index_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    def remove_p_zero(obj):
        if isinstance(obj, dict):
            # Remove "p" if its value is 0 or "0"
            if "p" in obj and (obj["p"] == 0 or obj["p"] == "0"):
                del obj["p"]
            # Recursively process nested dicts/lists
            for v in obj.values():
                remove_p_zero(v)
        elif isinstance(obj, list):
            for item in obj:
                remove_p_zero(item)

    remove_p_zero(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Processed: {file_path}")

def find_and_process_index_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "index.txt" in filenames:
            process_index_file(os.path.join(dirpath, "index.txt"))

if __name__ == "__main__":
    # Set this to your workspace root if running from elsewhere
    find_and_process_index_files(".")