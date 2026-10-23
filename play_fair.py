# Playfair cipher
def create_matrix(key):
    key = key.upper().replace("J", "I")
    chars = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in chars:
            chars += ch

    return [list(chars[i:i+5]) for i in range(0, 25, 5)]


def prepare_text(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace("J", "I")

    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            b = 'X'
            i += 1
        elif text[i] == text[i + 1]:
            b = 'X'
            i += 1
        else:
            b = text[i + 1]
            i += 2

        pairs.append(a + b)

    return pairs


def playfair(text, matrix, mode):
    result = ""

    for pair in prepare_text(text):
        a, b = pair
        r1, c1 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == a)
        r2, c2 = next((r, c) for r in range(5)
                      for c in range(5) if matrix[r][c] == b)

        if r1 == r2:  # Same row
            result += matrix[r1][(c1 + mode) % 5]
            result += matrix[r2][(c2 + mode) % 5]

        elif c1 == c2:  # Same column
            result += matrix[(r1 + mode) % 5][c1]
            result += matrix[(r2 + mode) % 5][c2]

        else:  # Rectangle rule
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(' '.join(row))

ciphertext = playfair(text, matrix, 1)
print("\nCiphertext:", ciphertext)

decrypted = playfair(ciphertext, matrix, -1)
print("Decrypted text:", decrypted)
