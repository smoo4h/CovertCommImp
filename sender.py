import sys
def string_to_binary(s):
    # Convert each character in the string to its ASCII value
    ascii_values = [ord(c) for c in s]
    
    # Convert the ASCII value to its binary representation (8-bit)
    binary_values = [format(value, '08b') for value in ascii_values]
    
    return "".join(binary_values)


def binary_to_file(binary_str, filename):
    # Replace '0' with a space and '1' with a tab
    formatted_string = binary_str.replace('0', ' ').replace('1', '\t')
    
    with open(filename, 'w') as file:
        file.write(formatted_string)


def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py [your message inside quotes]")
        return

    # Read binary from the file provided by the user
    s = sys.argv[1]
    binary_str = string_to_binary(s)
    
    # Save to a file, for instance, "output.txt"
    binary_to_file(binary_str, "message.txt")
    print("File saved as Message.txt")

if __name__ == "__main__":
    main()
