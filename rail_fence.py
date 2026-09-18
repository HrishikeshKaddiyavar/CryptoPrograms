def encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row] += char

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(ciphertext, rails):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(ciphertext)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]

    fence = []
    index = 0

    for count in counts:
        fence.append(list(ciphertext[index:index + count]))
        index += count

    result = ""
    positions = [0] * rails

    for row in pattern:
        result += fence[row][positions[row]]
        positions[row] += 1

    return result


plaintext = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

ciphertext = encrypt(plaintext, rails)
decrypted = decrypt(ciphertext, rails)

print("\nPlaintext :", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)


