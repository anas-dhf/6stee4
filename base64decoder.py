from base64 import b64decode
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
    # Get the path for the encoded file
    encoded_file_path = get_resource_path("encoded.txt")
    with open(encoded_file_path, "r") as file:
        toDecode = file.read()

    decoded = b64decode(toDecode)

    # Get the path for the decoded file
    decoded_file_path = get_resource_path("decoded.txt")
    with open(decoded_file_path, "w") as filee:
        filee.write(f'{decoded.decode()}')  # Decode bytes to string

except Exception as e:
    print(f"An error occurred: {e}")
