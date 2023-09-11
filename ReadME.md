# Covert Channel Scripts

This repository contains two Python scripts:

1. **Sender Script**: This script encodes a given string into a file using a specific format with spaces and tabs, simulating the process of sending a message.
2. **Receiver Script**: This script decodes the content of a given file that was previously encoded using the sender script, simulating the process of receiving a message.

## Prerequisites

- Python 3.x installed.

## Instructions

### Sender

1. The sender script is named `sender_script_name.py` (Please replace `sender_script_name.py` with your actual filename if different).
   
2. To send (encode) a message, run the script from your terminal or command prompt as follows:

   ```bash
   python sender_script_name.py "Your Message Here"
   ```

   Replace "Your Message Here" with the message you want to send (encode). Make sure your message is enclosed in double quotes.

3. Once the script is run successfully, a file named `message.txt` will be created in the same directory. This file contains the sent (encoded) format of your message.

### Receiver

1. The receiver script is named `receiver_script_name.py` (Please replace `receiver_script_name.py` with your actual filename if different).
   
2. To receive (decode) a message from a previously sent (encoded) file, run the script as follows:

   ```bash
   python receiver_script_name.py path_to_file.txt
   ```

   Replace `path_to_file.txt` with the path to your sent (encoded) file. If you're decoding the `message.txt` created by the sender script and it's in the same directory, use:

   ```bash
   python receiver_script_name.py message.txt
   ```

3. After successfully running the script, the received (decoded) message will be printed on the console.

## Notes

- Make sure both scripts are in the same directory as the file you want to receive (decode) or where you want to send (encode) the message, or provide the necessary path when calling them.
- These scripts are sensitive to file content. Ensure that the file to be received (decoded) contains only the sent (encoded) content and nothing else.

