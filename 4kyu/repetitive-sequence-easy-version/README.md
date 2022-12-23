# Repetitive Sequence  - Easy Version 

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 5f134651bc9687000f8022c4                              |
| Name:      | Repetitive Sequence  - Easy Version                             |
| Slug:      | repetitive-sequence-easy-version                            |
| Rank:      | 4 kyu                       |
| URL:       | [https://www.codewars.com/kata/5f134651bc9687000f8022c4](https://www.codewars.com/kata/5f134651bc9687000f8022c4)                 |
| Languages: |  `python`  `javascript`  |

---
## Description

_Yet another easy kata!_


# Task:
  
  
  - Let's write a sequence starting with `seq = [0, 1, 2, 2]` in which
      - 0 and 1 occurs 1 time
      - 2 occurs 2 time
  
  
  and sequence advances with adding next natural number `seq[natural number]` times so now, 3 appears 
  2 times and so on.
  
  ### Input
   - You are given input `n`  and return nth(0-based) value of this list.
  
  
  let;s take example:
  
  seq = [0, 1, 2, 2]\
  i = 3 and as seq[i]=2, seq = [0, 1, 2, 2, 3, 3]\
  i = 4 and as seq[i]=3, seq = [0, 1, 2, 2, 3, 3, 4, 4, 4]\
  i = 5 and as seq[i]=3, seq = [0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
  and so on.
  
  Some elements of list:
  ```
[0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21]
  ```
  <hr>
  
  # Constraint :
  
  
  * Python
    - 0 <= n <= `$2^{41}$`
  * Javascript
    - 0 <= n <= `$2^{49}$`
  
  
  <hr>

##### Have fun!

_tip: you can solve this using smart brute-force._ 

---
