# Vowels Back

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 57cfd92c05c1864df2001563                              |
| Name:      | Vowels Back                            |
| Slug:      | vowels-back                            |
| Rank:      | 6 kyu                       |
| URL:       | [https://www.codewars.com/kata/57cfd92c05c1864df2001563](https://www.codewars.com/kata/57cfd92c05c1864df2001563)                 |
| Languages: |  `javascript`  `haskell`  `ruby`  `python`  `c`  `rust`  `julia`  `crystal`  `coffeescript`  `r`  `nim`  `typescript`  |

---
## Description

You need to play around with the provided string (s).

Move consonants forward 9 places through the alphabet.
If they pass 'z', start again at 'a'.

Move vowels back 5 places through the alphabet.
If they pass 'a', start again at 'z'.
For our Polish friends this kata does not count 'y' as a vowel.

Exceptions:

If the character is 'c' or 'o', move it back 1 place.
For 'd' move it back 3, and for 'e', move it back 4.

If a moved letter becomes 'c', 'o', 'd' or 'e', revert it back to it's original value.

Provided string will always be lower case, won't be empty and will have no special characters.

---
