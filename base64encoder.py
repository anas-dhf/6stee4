from base64 import b64encode
import os
import sys

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Running in a bundled executable
        base_path = sys._MEIPASS
    else:
        # Running in a normal Python environment
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

try:
    userStr = input("Text to encode: ")
    encoded = b64encode(userStr.encode()).decode()
    
    # Get the path for the encoded file
    file_path = get_resource_path("encoded.txt")

    with open(file_path, "w") as file:
        file.write(encoded)
    
    print("File created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
