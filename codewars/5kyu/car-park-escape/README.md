# Car Park Escape

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 591eab1d192fe0435e000014                              |
| Name:      | Car Park Escape                            |
| Slug:      | car-park-escape                            |
| Rank:      | 5 kyu                       |
| URL:       | [https://www.codewars.com/kata/591eab1d192fe0435e000014](https://www.codewars.com/kata/591eab1d192fe0435e000014)                 |
| Languages: |  `ruby`  `python`  `javascript`  `csharp`  `fsharp`  `typescript`  `php`  `cpp`  |

---
## Description

## Introduction

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">A multi-storey car park (also called a parking garage, parking structure, parking ramp, parkade, parking building, parking deck or indoor parking) is a building designed for car parking and where there are a number of floors or levels on which parking takes place. It is essentially an indoor, stacked car park. Parking structures may be heated if they are enclosed.

Design of parking structures can add considerable cost for planning new developments, and can be mandated by cities or states in new building parking requirements. Some cities such as London have abolished previously enacted minimum parking requirements (Source <a href="https://en.wikipedia.org/wiki/Multi-storey_car_park">Wikipedia</a>)
</pre>

<center><img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/carpark.jpg"></center>

## Task

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
</pre>

## Rules

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
1. You are passed the carpark data as an argument into the function.<br>
2. Free carparking spaces are represented by a <span style="color:#A1A85E">0</span><br>
3. Staircases are represented by a <span style="color:#A1A85E">1</span><br>
4. Your parking place (start position) is represented by a <span style="color:#A1A85E">2</span> which could be on any floor.<br>
5. The exit is always the far right element of the ground floor.<br>
6. You must use the staircases to go down a level.<br>
7. You will never start on a staircase.<br>
8. The start level may be any level of the car park.<br>
9. Each floor will have only one staircase apart from the ground floor which will not have any staircases.</pre>

## Returns

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
Return an array of the quickest route out of the carpark<br>
<span style="color:#A1A85E">R1</span> = Move Right one parking space.<br>
<span style="color:#A1A85E">L1</span> = Move Left one parking space.<br>
<span style="color:#A1A85E">D1</span> = Move Down one level.
</pre>

## Example

### Initialise

```ruby
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
```
```python
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
```
```javascript
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]];
```
```csharp
Kata kata = new Kata();
int[,] carpark = new int[,] { { 1, 0, 0, 0, 2 },
                              { 0, 0, 0, 0, 0 } };
```                                       
```fsharp
let carpark = 
    [[1; 0; 0; 0; 2]
     [0; 0; 0; 0; 0]]
```
```c
carpark = {{1, 0, 0, 0, 2},
           {0, 0, 0, 0, 0}}
```
```cpp
carpark = {{1, 0, 0, 0, 2},
           {0, 0, 0, 0, 0}}
```
```java
carpark = {{1, 0, 0, 0, 2},
           {0, 0, 0, 0, 0}}
```
### Working Out

<pre style="white-space: pre-wrap;white-space: -moz-pre-wrap;white-space: -pre-wrap;white-space: -o-pre-wrap;word-wrap: break-word;">
- You start in the most far right position on level 1
- You have to move Left 4 places to reach the staircase => "<span style="color:#A1A85E">L4</span>"
- You then go down one flight of stairs => "<span style="color:#A1A85E">D1</span>"
- To escape you have to move Right 4 places => "<span style="color:#A1A85E">R4</span>"
</pre>

### Result

```ruby
result = ["L4", "D1", "R4"]
```
```python
result = ["L4", "D1", "R4"]
```
```javascript
result = ["L4", "D1", "R4"]
```
```csharp
string[] result = new string[] { "L4", "D1", "R4" };
```
```fsharp
let result = ["L4"; "D1"; "R4"]
```
```c
result = {"L4", "D1", "R4"}
```
```cpp
result = {"L4", "D1", "R4"}
```
```java
result = {"L4", "D1", "R4"}
```

Good luck and enjoy!<br>

## Kata Series

If you enjoyed this, then please try one of my other Katas. Any feedback, translations and grading of beta Katas are greatly appreciated. Thank you.

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58663693b359c4a6560001d6" target="_blank">Maze Runner</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58693bbfd7da144164000d05" target="_blank">Scooby Doo Puzzle</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/7KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586a1af1c66d18ad81000134" target="_blank">Driving License</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586c0909c1923fdb89002031" target="_blank">Connect 4</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/586e6d4cb98de09e3800014f" target="_blank">Vending Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/587136ba2eefcb92a9000027" target="_blank">Snakes and Ladders</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58a848258a6909dd35000003" target="_blank">Mastermind</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58b2c5de4cf8b90723000051" target="_blank">Guess Who?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Am I safe to drive?</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58f5c63f1e26ecda7e000029" target="_blank">Mexican Wave</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e" target="_blank">Pigs in a Pen</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/590300eb378a9282ba000095" target="_blank">Hungry Hippos</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/5904be220881cb68be00007d" target="_blank">Plenty of Fish in the Pond</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/590adadea658017d90000039" target="_blank">Fruit Machine</a></span>

<span style="display: flex !important;"><img style="margin:0px;" src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/6KYU.png" alt="Rank"/>&nbsp;<a href="https://www.codewars.com/kata/591eab1d192fe0435e000014" target="_blank">Car Park Escape</a></span>

---
