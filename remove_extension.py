import json

path = "results.json"
output_path = "transform_results.json"


def load_json_data(file_path: str):
    with open(file_path, "r") as f:
        print(f"Loading data from {file_path}")
        return json.load(f)


# Function to remove .webp extension from filenames
def remove_webp_extension(file_list):
    return [file[:-5] if file.endswith(".webp") else file for file in file_list]


# Function to save JSON data to a file
def save_json_data(data, file_path: str):
    with open(file_path, "w") as f:
        print(f"Writing data to {file_path}")
        json.dump(data, f, indent=2)


# Load JSON data
data = load_json_data(path)

# Iterate over the JSON data and update the values
for key in data:
    data[key] = remove_webp_extension(data[key])

# Output the modified JSON data to a new file
save_json_data(data, output_path)
