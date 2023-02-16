import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("string", 2) == "gnir_ts"
    assert encrypt_message("string", 3) == "rts_gni"
    assert encrypt_message("string", 10) == "gnirts"

    with pytest.raises(TypeError):
        encrypt_message(2, "string")
