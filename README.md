# Lab: 18 - Cryptography

## Authors:

_**Leo Kukharau**_

## Feature Tasks and Requirements

- Create an encrypt function that takes in a plain text phrase and a numeric shift.
  the phrase will then be shifted that many letters.
  - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
    shifts that exceed 26 should wrap around
  - E.g. encrypt(‘abc’,27) would return ‘bcd’
- Create a decrypt method that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form as long as correct key is supplied.
- Break the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.

## Dependencies

- python = "^3.8"
- pytest = "^6.0.0"
- pyenchant = "^3.1.1"

### Dev dependencies

- autopep8 = "^1.5.3"

[Link to code](./web_scraper/scraper.py)

[Link to PR](https://github.com/LeoKuhorev/caesar-cipher/pull/2)
