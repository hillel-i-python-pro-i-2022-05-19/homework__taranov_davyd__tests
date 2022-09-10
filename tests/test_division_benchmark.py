import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from app import encryption_or_decryption_caesar


@pytest.mark.parametrize(
    "cipher_text,shift_key,encryption_or_decryption_bool, result",
    [
        ("Hello! I'm Mike, I'm 30 years.", 13, True, "Uryyb! V'z Zvxr, V'z 07 lrnef."),
        ("Hello! I'm Mike, I'm 30 years.", -13, True, "Uryyb! V'z Zvxr, V'z 07 lrnef."),
        ("Hello! I'm Mike, I'm 30 years.", 0, True, "Hello! I'm Mike, I'm 30 years."),
        ("Uryyb! V'z Zvxr, V'z 07 lrnef.", 13, False, "Hello! I'm Mike, I'm 30 years."),
        ("Uryyb! V'z Zvxr, V'z 07 lrnef.", -13, False, "Hello! I'm Mike, I'm 30 years."),
        ("Hello! I'm Mike, I'm 30 years.", 0, False, "Hello! I'm Mike, I'm 30 years."),
    ],
)
def test_division_good(
    cipher_text: str, shift_key: int, encryption_or_decryption_bool: bool, result: str, benchmark: BenchmarkFixture
):
    result_ = benchmark(
        encryption_or_decryption_caesar,
        cipher_text,
        shift_key,
        encryption_or_decryption_bool,
    )
    assert result_ == result
