# Codebusters API
An API to generate Aristocrats and Patristocrats for Codebusters with K1, K2, and random substitution
encoding. Access the API [here](https://codebustersapi.pythonanywhere.com) (requires an endpoint)

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

## URL Parameters
`alphabet` - Random, K1, K2, K3 (defaults to Random)
> **_Note:_**  Keywords for xenocrypts will always be in English

Example calls:
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

Credit to [Codebuilder](https://github.com/AC01010/codebuilder) for [quotes list](quotes.txt) and
[keyword list](keywords.txt)
