# Format a string of names like 'Bart, Lisa & Maggie'.

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 53368a47e38700bd8300030d                              |
| Name:      | Format a string of names like 'Bart, Lisa & Maggie'.                            |
| Slug:      | format-a-string-of-names-like-bart-lisa-and-maggie                            |
| Rank:      | 6 kyu                       |
| URL:       | [https://www.codewars.com/kata/53368a47e38700bd8300030d](https://www.codewars.com/kata/53368a47e38700bd8300030d)                 |
| Languages: |  `ruby`  `javascript`  `python`  `elixir`  |

---
## Description

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

``` ruby
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
# returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
# returns 'Bart'

list([])
# returns ''
```
``` elixir
list([ %{name: "Bart"}, %{name: "Lisa"}, %{name: "Maggie"} ])
# returns 'Bart, Lisa & Maggie'

list([ %{name: "Bart"}, %{name: "Lisa"} ])
# returns 'Bart & Lisa'

list([ %{name: "Bart"} ])
# returns 'Bart'

list([])
# returns ''
```
``` javascript
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''
```
```python
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
```

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.


---
