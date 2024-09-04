import os
import sys
from base64 import b64encode, b64decode

def options():
    print("1: Encode")
    print("2: Decode")
    print("3: Print Everything")
    print("4: Exit")

def encode():
    try:
        userStr = input("Text to encode: ")
        encoded = b64encode(userStr.encode()).decode()
        
        # Create the encoded file in the current working directory
        with open("encoded.txt", "w") as file:
            file.write(encoded)
        
        print("File created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def decode():
    try:
        # Check if encoded.txt exists
        if not os.path.exists("encoded.txt"):
            print("Error: encoded.txt not found!")
            return
        
        # Read from the encoded file and decode
        with open("encoded.txt", "r") as file:
            toDecode = file.read()

        decoded = b64decode(toDecode).decode()

        # Write the decoded result to decoded.txt
        with open("decoded.txt", "w") as filee:
            filee.write(decoded)
        
        print("Decoded successfully and saved to decoded.txt!")

    except Exception as e:
        print(f"An error occurred: {e}")

def print_everything():
    try:
        if not os.path.exists("encoded.txt") or not os.path.exists("decoded.txt"):
            print("Error: Either encoded.txt or decoded.txt not found!")
            return
        
        with open("encoded.txt", "r") as enc_file:
            encodedData = enc_file.read()
        
        with open("decoded.txt", "r") as dec_file:
            decodedData = dec_file.read()

        print(f"Encoded: {encodedData}")
        print(f"Decoded: {decodedData}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main Execution Loop
if __name__ == "__main__":
    value = 0
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
            encode()
            print("----------")

        elif value == 2:
            decode()
            print("----------")

        elif value == 3:
            print_everything()
            print("----------")

        elif value == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid option!")
