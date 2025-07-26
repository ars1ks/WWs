def create_hex_mapping(shift, key):
    mapping = {}
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*() "
    alphabet = shuffle_alphabet(alphabet, key)
    index = 0
    start_row = shift // 16
    start_col = shift % 16

    for row in range(start_row, 16):
        for col in range(start_col, 16):
            cell = f"{hex(row)[2:].upper()}{hex(col)[2:].upper()}"
            if index < len(alphabet):
                mapping[cell] = alphabet[index]
                index += 1
            else:
                break
        start_col = 0
    return mapping

def shuffle_alphabet(alphabet, key):
    seed = sum(ord(char) for char in key)
    alphabet_list = list(alphabet)
    import random
    random.seed(seed)
    random.shuffle(alphabet_list)
    return "".join(alphabet_list)

def decrypt_message(encrypted_message, mapping):
    decrypted_message = []
    i = 0
    n = len(encrypted_message)
    
    while i < n:
        if encrypted_message[i] in "0123456789ABCDEF":
            cell = encrypted_message[i:i+2]
            i += 2
            if cell in mapping:
                decrypted_message.append(mapping[cell])
            else:
                decrypted_message.append(cell)
        else:
            decrypted_message.append(encrypted_message[i])
            i += 1
    
    return "".join(decrypted_message)

def main():
    shift = int(input("Введите сдвиг (например, 5): ").strip())

    key = input("Введите используемый ключ: ".strip())

    mapping = create_hex_mapping(shift, key)
    encrypted_message = input("\nВведите зашифрованное сообщение: ").strip()
    decrypted_message = decrypt_message(encrypted_message, mapping)
    print(f"Расшифрованное сообщение: {decrypted_message}")

if __name__ == "__main__":
    main()