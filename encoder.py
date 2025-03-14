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

def display_board(mapping):
    print("\nДоска 16x16:")
    print("   " + " ".join(hex(i)[2:].upper() for i in range(16)))  
    for row in range(16):
        row_label = hex(row)[2:].upper()
        print(f"{row_label}: ", end="")
        for col in range(16):
            cell = f"{row_label}{hex(col)[2:].upper()}"
            if cell in mapping:
                print(f"{mapping[cell]:<2}", end=" ") 
            else:
                print("  ", end=" ") 
        print()

def encrypt_message(message, mapping):
    encrypted_message = []
    reverse_mapping = {v: k for k, v in mapping.items()} 
    for char in message.upper():
        if char in reverse_mapping:
            encrypted_message.append(reverse_mapping[char])
        else:
            encrypted_message.append(char)
    return "".join(encrypted_message)

def main():
    shift = int(input("Введите сдвиг (например, 5): ").strip())
    key = ""
    print(f"Используемый ключ: {key}")
    
    mapping = create_hex_mapping(shift, key)
    display_board(mapping)

    message = input("\nСообщение: ").strip()
    encrypted_message = encrypt_message(message, mapping)
    print(f" {encrypted_message}")


if __name__ == "__main__":
    main()