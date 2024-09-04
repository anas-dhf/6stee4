import subprocess
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
    post_decode_path = get_resource_path("post-decode-read.py")
    subprocess.run(['python', post_decode_path])
except Exception as e:
    print(f"An error occurred: {e}")
