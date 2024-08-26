def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts the input text using the Caesar Cipher algorithm.

    Parameters:
    - text (str): The input text to encrypt or decrypt.
    - shift (int): The number of positions each letter is shifted.
    - mode (str): 'encrypt' for encryption and 'decrypt' for decryption.

    Returns:
    - str: The resulting encrypted or decrypted text.
    """
    result = []

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    # Iterate through each character in the text
    for char in text:
        # Check if character is a letter
        if char.isalpha():
            # Determine the ASCII offset based on whether it's uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Compute the shifted character
            shifted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            result.append(shifted_char)
        else:
            # Non-alphabetical characters remain unchanged
            result.append(char)

    # Join the list into a string and return the result
    return ''.join(result)

if __name__ == "__main__":
    # Prompt the user for input
    mode = input("Would you like to 'encrypt' or 'decrypt' the message? ").strip().lower()
    message = input("Enter your message: ")
    shift_value = int(input("Enter the shift value (e.g., 3): "))

    # Perform the operation
    if mode in ['encrypt', 'decrypt']:
        result = caesar_cipher(message, shift_value, mode)
        print(f"Result: {result}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
