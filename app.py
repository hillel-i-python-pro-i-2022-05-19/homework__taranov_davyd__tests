def encryption_or_decryption_caesar(cipher_text: str, shift_key: int, encryption_or_decryption_bool: bool) -> str:
    shift_key = abs(shift_key) if encryption_or_decryption_bool else -abs(shift_key)
    result_text = ""
    for symbol in cipher_text:
        if symbol.islower():
            symbol_index = ord(symbol) - ord("a")
            symbol_shifted = chr((symbol_index - shift_key) % 26 + ord("a"))
            result_text += symbol_shifted
        elif symbol.isupper():
            symbol_index = ord(symbol) - ord("A")
            symbol_index_shifted = (symbol_index - shift_key) % 26 + ord("A")
            symbol_shifted = chr(symbol_index_shifted)
            result_text += symbol_shifted
        elif symbol.isdigit():
            symbol_shifted = (int(symbol) - shift_key) % 10
            result_text += str(symbol_shifted)
        else:
            result_text += symbol
    return result_text
