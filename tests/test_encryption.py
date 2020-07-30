import pytest

from caesar_cipher import encryption as enc


class TestEncryption:

    def test_proof_of_life(self):
        assert enc

    message_1 = 'It was the best of times, it was the worst of times.'
    message_2 = '111 is greater than 333 (obviously)'
    message_3 = '[JuSt ChEcKiNg the special *characters!]'

    test_non_zero = (
        # Positive keys below 94
        (message_1, 1),
        (message_2, 4),
        (message_3, 55),

        # Positive keys above 94
        (message_1, 456),
        (message_2, 223),
        (message_3, 46457),

        # Negative keys below 94
        (message_1, -12),
        (message_2, -2),
        (message_3, -3),

        # Negative keys above 94
        (message_1, -234),
        (message_2, -421),
        (message_3, -300),
    )

    test_zero = (
        (message_1, 0),
        (message_2, 0),
        (message_3, 0),
    )

    test_is_broken = (
        (message_1, 100.0),
        (message_2, 71.43),
        (message_3, 71.43),
    )

    @pytest.mark.parametrize('msg, key', test_non_zero)
    def test_encrypt_non_zero(self, msg, key):
        assert enc.encrypt(msg, key) != msg

    @pytest.mark.parametrize('msg, key', test_zero)
    def test_encrypt_zero(self, msg, key):
        assert enc.encrypt(msg, key) == msg

    @pytest.mark.parametrize('msg, key', test_non_zero)
    def test_decrypt_non_zero(self, msg, key):
        enc_msg = enc.encrypt(msg, key)
        assert enc.decrypt(enc_msg, key) == msg

    @pytest.mark.parametrize('msg, key', test_zero)
    def test_decrypt_zero(self, msg, key):
        enc_msg = enc.encrypt(msg, key)
        assert enc.decrypt(enc_msg, key) == msg

    @pytest.mark.parametrize('msg, key', test_non_zero)
    def test_break_non_zero(self, msg, key):
        enc_msg = enc.encrypt(msg, key)
        assert enc.break_code(enc_msg, 'en') == msg

    @pytest.mark.parametrize('msg, key', test_zero)
    def test_break_zero(self, msg, key):
        enc_msg = enc.encrypt(msg, key)
        assert enc.break_code(enc_msg, 'en') == msg

    @pytest.mark.parametrize('msg, percentage', test_is_broken)
    def test_is_broken(self, msg, percentage):
        enc_msg = enc.encrypt(msg, 5)
        dec_msg = enc.break_code(enc_msg, 'en')

        actual = enc.is_broken(dec_msg, 'en')
        expected = f'The chance that the message is decrypted - {percentage}%'

        assert actual == expected
