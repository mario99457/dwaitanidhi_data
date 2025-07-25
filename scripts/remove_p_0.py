import os
import json

def collect_a_values(obj, a_values):
    if isinstance(obj, dict):
        if "a" in obj:
            a_values.add(obj["a"])
        for v in obj.values():
            collect_a_values(v, a_values)
    elif isinstance(obj, list):
        for item in obj:
            collect_a_values(item, a_values)

def remove_p_zero_and_a(obj, remove_a):
    if isinstance(obj, dict):
        if "p" in obj and (obj["p"] == 0 or obj["p"] == "0"):
            del obj["p"]
        if remove_a and "a" in obj: #"a" is not directly inside obj. it is 
            del obj["a"]
        for v in obj.values():
            remove_p_zero_and_a(v, remove_a)
    elif isinstance(obj, list):
        for item in obj:
            remove_p_zero_and_a(item, remove_a)

def process_index_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collect all "a" values
    a_values = set()
    collect_a_values(data, a_values)
    remove_a = len(a_values) == 1 and len(a_values) > 0

    # Remove "p": 0 and "a" if needed
    remove_p_zero_and_a(data, remove_a)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Processed: {file_path}")

def find_and_process_index_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "index.txt" in filenames:
            process_index_file(os.path.join(dirpath, "index.txt"))

if __name__ == "__main__":
    find_and_process_index_files(".")