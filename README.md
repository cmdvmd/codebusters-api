# Codebusters API

An API to generate Aristocrats and Patristocrats for Codebusters with K1, K2, and random substitution
encoding. Access the API [here](https://codebustersapi.pythonanywhere.com) (requires an endpoint)

## Endpoints

* `aristocrat`
* `patristocrat`

Example Calls:

```
https://codebustersapi.pythonanywhere.com/aristocrat
```

```
https://codebustersapi.pythonanywhere.com/patristocrat
```

## URL Parameters

`alphabet` - K1, K2, Random (defaults to Random)

Example calls:

```
https://codebustersapi.pythonanywhere.com/aristocrat?alphabet=K1
```

```
https://codebustersapi.pythonanywhere.com/patristocrat?alphabet=K2
```

## Response

Example response:

```json
{
  "ciphertext": "D NDPW LEW ZKWMYH FQ LEW QILIKW CWLLWK LEMU LEW EDHLFKB FQ LEW OMHL.",
  "frequency": {
    "A": 0,
    "B": 1,
    "C": 1,
    "D": 3,
    "E": 6,
    "F": 3,
    "G": 0,
    "H": 3,
    "I": 2,
    "J": 0,
    "K": 4,
    "L": 10,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 1,
    "Q": 3,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 1,
    "V": 0,
    "W": 9,
    "X": 0,
    "Y": 1,
    "Z": 1
  },
  "plaintext": "I LIKE THE DREAMS OF THE FUTURE BETTER THAN THE HISTORY OF THE PAST."
}
```

* `ciphertext` - The encrypted text of the problem
* `plaintext` - The original quote from the problem
* `frequency` - The number of occurrences of each letter in the ciphertext


## Development
To further develop this api, make sure to install `Flask~=2.2.3` from Pip

## Credits

Credit to [Codebuilder](https://github.com/AC01010/codebuilder) for [quotes list](quotes.txt) and
[keyword list](keywords.txt)
