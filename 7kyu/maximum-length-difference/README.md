# Maximum Length Difference

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 5663f5305102699bad000056                              |
| Name:      | Maximum Length Difference                            |
| Slug:      | maximum-length-difference                            |
| Rank:      | 7 kyu                       |
| URL:       | [https://www.codewars.com/kata/5663f5305102699bad000056](https://www.codewars.com/kata/5663f5305102699bad000056)                 |
| Languages: |  `ruby`  `python`  `javascript`  `coffeescript`  `csharp`  `haskell`  `java`  `clojure`  `cpp`  `php`  `crystal`  `c`  `typescript`  `fsharp`  `shell`  `ocaml`  `kotlin`  `elixir`  `julia`  `r`  `scala`  `powershell`  `go`  `nim`  `rust`  `reason`  `racket`  `haxe`  `pascal`  `perl`  `d`  `cobol`  `erlang`  |

---
## Description

You are given two arrays `a1` and `a2` of strings. Each string is composed with letters from `a` to `z`.
Let `x` be any string in the first array and `y` be any string in the second array. 

  `Find max(abs(length(x) − length(y)))`

If `a1` and/or `a2` are empty return `-1` in each language
except in Haskell (F#) where you will return `Nothing` (None).

#### Example:
```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

```

#### Bash note:
 - input : 2 strings with substrings separated by `,`
 - output: number as a string

---
