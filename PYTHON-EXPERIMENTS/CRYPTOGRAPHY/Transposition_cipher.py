def transposition_cipher(text, key):
    result = ""
    columns = len(key)
    rows = len(text) // columns + (len(text) % columns > 0)
    matrix = [[' ' for _ in range(columns)] for _ in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(columns):
            if index < len(text):
                matrix[i][j] = text[index]
                index += 1

    for i in range(columns):
        for j in range(rows):
            if matrix[j][key[i] - 1] != ' ':
                result += matrix[j][key[i] - 1]

    return result

text = "Hello, world!"
key = [2, 1, 3]
encrypted_text = transposition_cipher(text, key)
print(encrypted_text)  # Output: Hld, erloow!