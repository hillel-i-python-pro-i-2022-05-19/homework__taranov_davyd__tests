import pytest

from app import encryption_or_decryption_caesar


@pytest.mark.parametrize(
    "cipher_text,shift_key,encryption_or_decryption_bool,result",
    [
        ("Uryyb! V'z Zvxr, V'z 07 lrnef.", 13, False, "Hello! I'm Mike, I'm 30 years."),
        ("Uryyb! V'z Zvxr, V'z 07 lrnef.", -13, False, "Hello! I'm Mike, I'm 30 years."),
        ("Hello! I'm Mike, I'm 30 years.", 0, False, "Hello! I'm Mike, I'm 30 years."),
        ("Hello! I'm Mike, I'm 30 years.", 0, False, "Hello! I'm Mike, I'm 30 years."),
        ("Hello! I'm Mike, I'm 30 years.", 13, True, "Uryyb! V'z Zvxr, V'z 07 lrnef."),
        ("Hello! I'm Mike, I'm 30 years.", -13, True, "Uryyb! V'z Zvxr, V'z 07 lrnef."),
        ("Hello! I'm Mike, I'm 30 years.", 0, True, "Hello! I'm Mike, I'm 30 years."),
    ],
)
def test_division(
    cipher_text: str,
    shift_key: int,
    encryption_or_decryption_bool: bool,
    result: str,
):
    assert (
        encryption_or_decryption_caesar(
            cipher_text=cipher_text, shift_key=shift_key, encryption_or_decryption_bool=encryption_or_decryption_bool
        )
        == result
    )


cipher_text_start = "Hello! I'm Mike, I'm 30 years."


@pytest.mark.parametrize(
    "cipher_text,shift_key,encryption_or_decryption_bool_true,encryption_or_decryption_bool_false,result",
    [
        (cipher_text_start, 13, True, False, cipher_text_start),
    ],
)
def data_loss_check(
    cipher_text: str,
    shift_key: int,
    encryption_or_decryption_bool_true: bool,
    encryption_or_decryption_bool_false: bool,
):
    assert (
        encryption_or_decryption_caesar(
            cipher_text=encryption_or_decryption_caesar(
                cipher_text=cipher_text,
                shift_key=shift_key,
                encryption_or_decryption_bool=encryption_or_decryption_bool_true,
            ),
            shift_key=shift_key,
            encryption_or_decryption_bool=encryption_or_decryption_bool_false,
        )
        == cipher_text
    )
