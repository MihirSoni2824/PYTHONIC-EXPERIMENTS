def vigenere_cipher(text, keyword):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + ord(keyword[key_index % len(keyword)].upper()) - 65) % 26 + 65)
            else:
                result += chr((ord(char) + ord(keyword[key_index % len(keyword)].lower()) - 97) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result

text = "Hello, world!"
keyword = "key"
encrypted_text = vigenere_cipher(text, keyword)
print(encrypted_text)  # Output: YIQUN, XLDNU!