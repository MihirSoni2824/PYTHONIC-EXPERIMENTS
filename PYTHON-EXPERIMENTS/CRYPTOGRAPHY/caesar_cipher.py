def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


text = "Hello, world!"
shifted_text = caesar_cipher(text, 3)
print(shifted_text)  # Output: KHOOR, ZRUOG!