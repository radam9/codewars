# Valid Parentheses

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 52774a314c2333f0a7000688                              |
| Name:      | Valid Parentheses                            |
| Slug:      | valid-parentheses                            |
| Rank:      | 5 kyu                       |
| URL:       | [https://www.codewars.com/kata/52774a314c2333f0a7000688](https://www.codewars.com/kata/52774a314c2333f0a7000688)                 |
| Languages: |  `javascript`  `coffeescript`  `haskell`  `python`  `ruby`  `dart`  `go`  `elixir`  `csharp`  `objc`  `nasm`  `c`  `java`  `cobol`  `julia`  `rust`  `d`  |

---
## Description

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= input.length <= 100`

~~~if-not:javascript,go,cobol
Along with opening (`(`) and closing (`)`) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do **not** treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
~~~


---
