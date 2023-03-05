"""
Credit to Codebuilder bot (https://github.com/AC01010/codebuilder) for quotes list
"""

import random
import string


def calculate_frequency(text):
    frequency = {}
    for letter in alphabet:
        frequency.update({letter: text.count(letter)})
    return frequency


def encode_random():
    # Generate key
    remaining = list(alphabet)
    key = {}
    for letter in alphabet:
        replacement = letter
        while replacement == letter:
            replacement = random.choice(remaining)
        key.update({letter: replacement})
        remaining.remove(replacement)

    # Encode quote
    plaintext = random.choice(quote_list)
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext, plaintext


def aristocrat():
    ciphertext, plaintext = encode_random()
    return {
        'ciphertext': ciphertext,
        'plaintext': plaintext,
        'frequency': calculate_frequency(ciphertext)
    }


def patristocrat():
    chunk_size = 5
    spaced_ciphertext, plaintext = encode_random()
    replace = str.maketrans('', '', string.punctuation + ' ')
    raw_chars = spaced_ciphertext.translate(replace)
    ciphertext = ' '.join([raw_chars[i: i + chunk_size] for i in range(0, len(raw_chars), chunk_size)])
    return {
        'ciphertext': ciphertext,
        'plaintext': plaintext,
        'frequency': calculate_frequency(ciphertext)
    }


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('quotes.txt', 'r', encoding='utf-8') as quotes_file:
    quote_list = [line.strip().upper() for line in quotes_file.readlines()]

print(patristocrat())
