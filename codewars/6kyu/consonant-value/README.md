# Consonant value

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 59c633e7dcc4053512000073                              |
| Name:      | Consonant value                            |
| Slug:      | consonant-value                            |
| Rank:      | 6 kyu                       |
| URL:       | [https://www.codewars.com/kata/59c633e7dcc4053512000073](https://www.codewars.com/kata/59c633e7dcc4053512000073)                 |
| Languages: |  `javascript`  `python`  `ruby`  `haskell`  `csharp`  `c`  `nasm`  `coffeescript`  `crystal`  `php`  `typescript`  `go`  `dart`  `cpp`  `java`  `elixir`  |

---
## Description

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except `"aeiou"`. 

We shall assign the following values: `a = 1, b = 2, c = 3, .... z = 26`.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z **~~o~~** d **~~ia~~** cs"

```haskell
-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
```

For C: do not mutate input.

More examples in test cases. Good luck!

If you like this Kata, please try:

[Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)

[Vowel-consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)

---
