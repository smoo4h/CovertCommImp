import sys
def file_to_binary(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Replace spaces with 0 and tabs with 1
    binary_str = content.replace(' ', '0').replace('\t', '1')
    return binary_str


def binary_to_string(binary_str):
    # Split the binary string into groups of 8 bits
    byte_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each 8-bit group to its ASCII value and then to its character representation
    char_list = [chr(int(byte, 2)) for byte in byte_list]
    
    return ''.join(char_list)


def main():
    # Read binary from the file, for instance, "output.txt"
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <filename>")
        return

    # Read binary from the file provided by the user
    filename = sys.argv[1]
    binary_str = file_to_binary(filename)
    
    # Convert binary to string
    decoded_str = binary_to_string(binary_str)
    print("The message is :",decoded_str)


if __name__ == "__main__":
    main()