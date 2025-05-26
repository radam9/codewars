# Integers: Recreation One

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 55aa075506463dac6600010d                              |
| Name:      | Integers: Recreation One                            |
| Slug:      | integers-recreation-one                            |
| Rank:      | 5 kyu                       |
| URL:       | [https://www.codewars.com/kata/55aa075506463dac6600010d](https://www.codewars.com/kata/55aa075506463dac6600010d)                 |
| Languages: |  `ruby`  `python`  `javascript`  `java`  `csharp`  `coffeescript`  `haskell`  `clojure`  `cpp`  `php`  `crystal`  `fsharp`  `c`  `typescript`  `rust`  `swift`  `go`  `r`  `shell`  `ocaml`  `elixir`  `fortran`  `julia`  `scala`  `powershell`  `nim`  `purescript`  `reason`  `racket`  `kotlin`  `prolog`  `pascal`  `factor`  `raku`  `vb`  `lua`  `perl`  `elm`  `d`  `erlang`  |

---
## Description

`1, 246, 2, 123, 3, 82, 6, 41` are the divisors of number `246`. Squaring these divisors we get: `1, 60516, 4, 15129, 9, 6724, 36, 1681`. The sum of these squares is `84100` which is `290 * 290`.

#### Task
Find all integers between `m` and `n` (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square. 

We will return an array of subarrays or of tuples (in C an array of Pair) or a string. 
The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

#### Example:
```
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
```
The form of the examples may change according to the language, see "Sample Tests".

#### Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.



---
