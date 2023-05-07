# Codebusters API

An API to generate Aristocrats and Patristocrats for Codebusters with K1, K2, and random substitution
encoding.

Current API hosted at: [codebustersapi.pythonanywhere.com](https://codebustersapi.pythonanywhere.com)

## Endpoints

* `aristocrat`
* `patristocrat`
* `xenocrypt`

Example Calls:

```
https://codebustersapi.pythonanywhere.com/aristocrat
```

```
https://codebustersapi.pythonanywhere.com/patristocrat
```

```
https://codebustersapi.pythonanywhere.com/xenocrypt
```

## Encoding with a Keyed Alphabet

Use the `alphabet` parameter with the value Random, K1, K2, or K3 (defaults to Random) to generate a problem that has
been encoded with the chosen alphabet

> **_Note:_**  Keywords for xenocrypts will always be in English

*Example calls:*

```
https://codebustersapi.pythonanywhere.com/aristocrat?alphabet=K1
```

```
https://codebustersapi.pythonanywhere.com/patristocrat?alphabet=K2
```

```
https://codebustersapi.pythonanywhere.com/xenocrypt?alphabet=K3
```

## Response

Example response:

```json
{
  "ciphertext": "D NDPW LEW ZKWMYH FQ LEW QILIKW CWLLWK LEMU LEW EDHLFKB FQ LEW OMHL.",
  "plaintext": "I LIKE THE DREAMS OF THE FUTURE BETTER THAN THE HISTORY OF THE PAST."
}
```

* `ciphertext` - The encrypted text of the problem
* `plaintext` - The original quote from the problem

## Credits

Credit to [Codebuilder](https://github.com/AC01010/codebuilder) for [quotes list](quotes.txt)
and [keyword list](keywords.txt)

## Development

To develop this project further, [fork](https://github.com/cmdvmd/codebusters-api/fork) this repository and install
dependencies from [`requirements.txt`](requirements.txt) using `pip`
