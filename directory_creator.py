import os
import json

def create_directory_structure(structure, base_path="."):
    """
    Recursively creates a directory structure based on a dictionary
    """
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        
        # If value is a dict, it's a directory with subdirectories/files
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_directory_structure(value, path)
        else:
            # Make sure the directory exists
            os.makedirs(os.path.dirname(path), exist_ok=True)
            
            # Create the file with initial content if provided
            with open(path, 'w') as f:
                if value:
                    f.write(value)
                else:
                    f.write("")


# Load the JSON file
json_file_path = "directory_structure.json"  # Adjust the path if needed
with open(json_file_path, 'r') as json_file:
    directory_structure = json.load(json_file)

# Print the directory structure for verification
print(json.dumps(directory_structure, indent=2))

# Uncomment the following line to actually create the structure
create_directory_structure(directory_structure)