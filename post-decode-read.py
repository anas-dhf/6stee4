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
    decoded_file_path = get_resource_path("decoded.txt")
    with open(decoded_file_path, "r") as file:
        decodedData = ''
        for line in file:
            if line.startswith("b'"):
                decodedData = line.split("'", 2)[1].strip()

    encoded_file_path = get_resource_path("encoded.txt")
    with open(encoded_file_path, "r") as filee:
        encodedData = filee.read()

    print(f"Encoded: {encodedData}")
    print(f"Decoded: {decodedData}")

except Exception as e:
    print(f"An error occurred: {e}")
