import re

import enchant


def encrypt(text: str, key: int) -> str:
    """Encrypt the given message by shifting each caracter by a given key

    Args:
        text (str): Message to be encrypted
        key (int): Shift value

    Returns:
        str: Encrypted message
    """
    ascii_codes = []
    for char in text:
        shifted_code = (ord(char) + key) % 94
        while shifted_code > 125:
            shifted_code -= 94
        while shifted_code < 31:
            shifted_code += 94
        ascii_codes.append(shifted_code)

    return ''.join(chr(code) for code in ascii_codes)


def decrypt(text: str, key: int) -> str:
    """Decrypt the given message by providing the encryption key

    Args:
        text (str): Encrypted message to be decrypted
        key (int): Encryption key

    Returns:
        str: Decrypted message
    """
    return encrypt(text, -key)


def break_code(encrypted_text: str, lang: str) -> str:
    """Decrypt the given message by bruteforcing the shift keys and picking the option with the highest percentage of words matching the given language

    Args:
        encrypted_text (str): Message to be decrypted
        lang (str): Language of the encrypted message

    Returns:
        str: Decrypted message
    """
    d = enchant.Dict(lang)

    # Store all options with at least 1 word matching the language
    options = {}

    # Try 94 keys to find the one that gives the best results
    for i in range(94):
        text = decrypt(encrypted_text, i)
        words = re.split('\W+', text)
        _len, _sum = len(words), 0

        # Check if there are any words matching the lang dictionary
        for word in words:
            if len(word) > 1:
                if d.check(word):
                    _sum += 1
        if _sum:
            options[_sum / _len] = i

    # Get the option with the higher match percentage
    key = sorted(options.keys(), reverse=True)[0]

    return decrypt(encrypted_text, options[key])


def is_broken(decrypted_message: str, lang: str) -> str:
    """Check if the passed in message is decrypted by matching the words of the message with a dict of the given language

    Args:
        decrypted_message (str): Decrypted message
        lang (str): Language of the message

    Returns:
        str: Message about the chances the message is decrypted
    """
    d = enchant.Dict(lang)
    words = re.split('\W+', decrypted_message)
    _len, _sum = len(words), 0

    for word in words:
        if word == '':
            _sum += 1
        elif len(word) > 1:
            if d.check(word):
                _sum += 1

    return f'The chance that the message is decrypted - {round(_sum * 100 / _len, 2)}%'
