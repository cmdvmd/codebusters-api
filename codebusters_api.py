import os
import random
import string
from flask import Flask, request
from flask_cors import CORS
from googletrans import Translator
from unidecode import unidecode

app = Flask(__name__)
CORS(app)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spanish_n = '\u00d1'
spanish_letters = f'ABCDEFGHIJKLMN{spanish_n}OPQRSTUVWXYZ'


def validate_alphabet(ciphertext, plaintext=letters):
    for i in range(len(ciphertext)):
        if ciphertext[i] == plaintext[i]:
            return False
    return True


def encode_quote(key, spanish=False):
    plaintext = random.choice(quote_list)
    if spanish:
        spanish_ignore = spanish_n + '\u00a1\u00bf'
        translated = translator.translate(plaintext, src='en', dest='es').text
        normalized = list(unidecode(translated))
        for index, char in enumerate(translated):
            if char in spanish_ignore:
                normalized[index] = char
        plaintext = ''.join(normalized)

    ciphertext = ''
    for char in plaintext:
        if char in letters or (spanish_n in key and char in spanish_letters):
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext, plaintext


def key_alphabet(keyword=None, alphabet=letters):
    keyword = keyword if keyword is not None else random.choice(keyword_list)
    keyword_unique = ''.join(dict.fromkeys(keyword))

    mask = str.maketrans('', '', keyword)
    remaining = alphabet.translate(mask)
    while True:
        offset = random.randint(0, 25)
        cutoff = len(alphabet) - offset
        keyed_alphabet = keyword_unique[cutoff:] + remaining[-offset:] + keyword_unique[:cutoff] + remaining[:-offset]
        if validate_alphabet(keyed_alphabet, alphabet):
            break
    return keyword, keyed_alphabet


def encode_random(alphabet):
    ciphertext_alphabet = list(alphabet)
    while not validate_alphabet(''.join(ciphertext_alphabet), alphabet):
        random.shuffle(ciphertext_alphabet)
    key = dict(zip(ciphertext_alphabet, alphabet))
    return key


def encode_k1(alphabet):
    keyword, ciphertext_alphabet = key_alphabet(alphabet=alphabet)
    key = dict(zip(ciphertext_alphabet, alphabet))
    return key


def encode_k2(alphabet):
    keyword, ciphertext_alphabet = key_alphabet(alphabet=alphabet)
    key = dict(zip(alphabet, ciphertext_alphabet))
    return key


def encode_k3(alphabet):
    keyword, plaintext_alphabet = key_alphabet(alphabet=alphabet)
    while True:
        keyword,  ciphertext_alphabet = key_alphabet(keyword=keyword, alphabet=alphabet)
        key = dict(zip(ciphertext_alphabet, plaintext_alphabet))
        if validate_alphabet(ciphertext_alphabet, plaintext_alphabet):
            break
    return key


def generate_problem(alphabet, spanish=False):
    if alphabet.lower() == 'k1':
        key = encode_k1(alphabet=spanish_letters if spanish else letters)
    elif alphabet.lower() == 'k2':
        key = encode_k2(alphabet=spanish_letters if spanish else letters)
    elif alphabet.lower() == 'k3':
        key = encode_k3(alphabet=spanish_letters if spanish else letters)
    else:
        key = encode_random(alphabet=spanish_letters if spanish else letters)
    return encode_quote(key, spanish)


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


@app.route('/xenocrypt', methods=['GET'])
def xenocrypt():
    ciphertext, plaintext = generate_problem(request.args.get('alphabet', ''), True)
    return {
        'ciphertext': ciphertext,
        'plaintext': plaintext
    }, 200


translator = Translator()
resource_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(resource_dir, 'quotes.txt'), 'r', encoding='utf-8') as quotes_file:
    quote_list = [line.strip().upper() for line in quotes_file.readlines()]
with open(os.path.join(resource_dir, 'keywords.txt'), 'r', encoding='utf-8') as keywords_file:
    keyword_list = [line.strip().upper() for line in keywords_file.readlines()]

if __name__ == '__main__':
    app.run()
