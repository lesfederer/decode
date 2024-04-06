Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def decode(message_file):
    """
    Reads an encoded message from a .txt file, decodes it, and returns the decoded text.

    Args:
        message_file (str): The path to the .txt file containing the encoded message.

    Returns:
        str: The decoded message.
    """

    with open(message_file, 'r') as file:
        lines = file.readlines()

    message_words = []
    current_line = 1  # The current line number in the pyramid 
    current_num = 1   # The expected number on the current line

    for line in lines:
        num, word = line.strip().split()  # Split into number and word
        if int(num) == current_num:
            message_words.append(word)
            current_line += 1
            current_num = (current_line * (current_line + 1)) // 2  # Calculate the next expected number

    return ' '.join(message_words)  # Join the message words with spaces

# Example Usage
if __name__ == '__main__':
    encoded_message = decode('message.txt')
    print(encoded_message)  # Output: I love computers
