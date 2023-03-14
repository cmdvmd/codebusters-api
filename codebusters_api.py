import os
import random
import string
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def validate_alphabet(ciphertext, plaintext=letters):
    for i in range(len(ciphertext)):
        if ciphertext[i] == plaintext[i]:
            return False
    return True


def encode_quote(key):
    plaintext = random.choice(quote_list)
    ciphertext = ''
    for char in plaintext:
        if char in letters:
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext, plaintext


def key_alphabet(keyword=None):
    keyword = keyword if keyword is not None else random.choice(keywords)
    keyword_unique = ''.join(dict.fromkeys(keyword))

    mask = str.maketrans('', '', keyword)
    remaining = letters.translate(mask)
    while True:
        offset = random.randint(0, 25)
        cutoff = len(letters) - offset
        keyed_alphabet = keyword_unique[cutoff:] + remaining[-offset:] + keyword_unique[:cutoff] + remaining[:-offset]
        if validate_alphabet(keyed_alphabet):
            break
    return keyword, keyed_alphabet


def encode_random():
    ciphertext_alphabet = list(letters)
    while not validate_alphabet(''.join(ciphertext_alphabet)):
        random.shuffle(ciphertext_alphabet)
    key = dict(zip(ciphertext_alphabet, letters))
    return key


def encode_k1():
    keyword, ciphertext_alphabet = key_alphabet()
    key = dict(zip(ciphertext_alphabet, letters))
    return key


def encode_k2():
    keyword, ciphertext_alphabet = key_alphabet()
    key = dict(zip(letters, ciphertext_alphabet))
    return key


def encode_k3():
    keyword, plaintext_alphabet = key_alphabet()
    while True:
        keyword,  ciphertext_alphabet = key_alphabet(keyword)
        key = dict(zip(ciphertext_alphabet, plaintext_alphabet))
        if validate_alphabet(ciphertext_alphabet, plaintext_alphabet):
            break
    return key


def generate_problem(alphabet):
    if alphabet.lower() == 'k1':
        key = encode_k1()
    elif alphabet.lower() == 'k2':
        key = encode_k2()
    elif alphabet.lower() == 'k3':
        key = encode_k3()
    else:
        key = encode_random()
    return encode_quote(key)


@app.route('/aristocrat', methods=['GET'])
def aristocrat():
    ciphertext, plaintext = generate_problem(request.args.get('alphabet', ''))
    return {
        'ciphertext': ciphertext,
        'plaintext': plaintext
    }, 200


@app.route('/patristocrat', methods=['GET'])
def patristocrat():
    chunk_size = 5
    punctuated_ciphertext, punctuated_plaintext = generate_problem(request.args.get('alphabet', ''))
    mask = str.maketrans('', '', string.punctuation + ' ')
    raw_ciphertext = punctuated_ciphertext.translate(mask)
    raw_plaintext = punctuated_plaintext.translate(mask)
    ciphertext = ' '.join([raw_ciphertext[i: i + chunk_size] for i in range(0, len(raw_ciphertext), chunk_size)])
    plaintext = ' '.join([raw_plaintext[i: i + chunk_size] for i in range(0, len(raw_plaintext), chunk_size)])
    return {
        'ciphertext': ciphertext,
        'plaintext': plaintext
    }, 200


resource_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(resource_dir, 'quotes.txt'), 'r', encoding='utf-8') as quotes_file:
    quote_list = [line.strip().upper() for line in quotes_file.readlines()]
with open(os.path.join(resource_dir, 'keywords.txt'), 'r', encoding='utf-8') as keywords_file:
    keywords = [line.strip().upper() for line in keywords_file.readlines()]

if __name__ == '__main__':
    app.run()
