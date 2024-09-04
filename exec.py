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

value = 0

def options(): 
    print("1: Encode")
    print("2: Decode")
    print("3: Print Everything")
    print("4: Exit")

print("*** Welcome to the encode/decode exec file! ***")

while value != 4:
    options()
    value = input(">> ")

    try:
        value = int(value)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if value == 1:
        encoder_path = get_resource_path("base64encoder.py")
        subprocess.run(['python', encoder_path])
        print("----------")

    elif value == 2:
        decoder_path = get_resource_path("base64decoder.py")
        subprocess.run(['python', decoder_path])
        print("----------")

    elif value == 3:
        printor_path = get_resource_path("printor.py")
        subprocess.run(['python', printor_path])
        print("----------")

    elif value == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
