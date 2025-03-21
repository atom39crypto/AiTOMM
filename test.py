import json

# File paths


# Get the new name from the user
new_name = input("Enter the new name to replace 'Unknown': ").strip()

# Process each file
def rename(new_name):
    file_paths = ["engine/Weilder/memory.json", "Impretion.json"]
    for file_path in file_paths:
        try:
            # Load the JSON file
            with open(file_path, "r") as file:
                data = json.load(file)

            # Check if "Unknown" exists in the JSON data
            if "Unknown" in data["users"]:
                # Update the key
                data["users"][new_name] = data["users"].pop("Unknown")

                # Save the updated JSON back to the file
                with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"Replaced 'Unknown' with '{new_name}' successfully in {file_path}.")
            else:
                print(f"'Unknown' key not found in {file_path}.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}")



if __name__ == "__main__":
    new_name = input("Enter the new name to replace 'Unknown': ")
    rename(new_name)