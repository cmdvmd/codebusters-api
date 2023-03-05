"""
Credit to Codebuilder bot (https://github.com/AC01010/codebuilder) for quotes list
"""

import random


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
    quote = random.choice(quote_list)
    encoded = ''
    for char in quote:
        if char in alphabet:
            encoded += key[char]
        else:
            encoded += char
    return encoded, quote


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('quotes.txt', 'r', encoding='utf-8') as quotes_file:
    quote_list = [line.strip().upper() for line in quotes_file.readlines()]
