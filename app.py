def encryption_or_decryption_caesar(cipher_text: str, shift_key: int, encryption_or_decryption_bool: bool) -> str:
    shift_key = abs(shift_key) if encryption_or_decryption_bool else -abs(shift_key)
    result_text = ""
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for symbol in cipher_text:
        if symbol.lower() in ru_alphabet:
            main_symbol_lower = "а"  # RU
            main_symbol_uppercase = "А"  # RU
            alphabet_length = 33
        else:
            main_symbol_lower = "a"  # EN
            main_symbol_uppercase = "A"  # EN
            alphabet_length = 26
        if symbol.islower():
            symbol_index = ord(symbol) - ord(main_symbol_lower)
            symbol_shifted = chr((symbol_index - shift_key) % alphabet_length + ord(main_symbol_lower))
            result_text += symbol_shifted
        elif symbol.isupper():
            symbol_index = ord(symbol) - ord(main_symbol_uppercase)
            symbol_index_shifted = (symbol_index - shift_key) % alphabet_length + ord(main_symbol_uppercase)
            symbol_shifted = chr(symbol_index_shifted)
            result_text += symbol_shifted
        elif symbol.isdigit():
            symbol_shifted = (int(symbol) - shift_key) % 10
            result_text += str(symbol_shifted)
        else:
            result_text += symbol
    return result_text
