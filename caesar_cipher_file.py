  def encrypt(text, shift):
    result = ""

    shift = shift % 26

    for c in text:
        if 'A' <= c <= 'Z':
            result += chr(
                ord('A') + (ord(c) - ord('A') + shift) % 26
            )
        else:
            result += c

    return result


def decrypt(text, shift):
    result = ""

    shift = shift % 26

    for c in text:
        if 'A' <= c <= 'Z':
            result += chr(
                ord('A') + (ord(c) - ord('A') - shift) % 26
            )
        else:
            result += c

    return result


def main():
    input_path = "input.txt"
    output_path = "output.txt"

    shift_input = input("Enter shift: ")

    try:
        shift = int(shift_input)
    except ValueError:
        print("Error: Shift must be a valid integer.")
        return

    try:
        with open(input_path, "r") as reader:
            text = reader.read().upper()

        # Encrypt the message
        encrypted_text = encrypt(text, shift)

        print("\nEncrypted text:")
        print(encrypted_text)

        # Decrypt the same encrypted message
        decrypted_text = decrypt(encrypted_text, shift)

        print("\nDecrypted text:")
        print(decrypted_text)

        # Save both results
        with open(output_path, "w") as writer:
            writer.write("Encrypted text:\n")
            writer.write(encrypted_text)

            writer.write("\n\nDecrypted text:\n")
            writer.write(decrypted_text)

        print("\nSuccess! Output saved to:", output_path)

    except FileNotFoundError:
        print("Error: Input file not found.")

    except OSError:
        print("Error: Could not access the file.")


main()

