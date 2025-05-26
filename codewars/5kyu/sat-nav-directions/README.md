# Sat Nav directions

---
## Info

|            |                                      |
|:-----------|:-------------------------------------|
| ID:        | 5a9b4d104a6b341b42000070                              |
| Name:      | Sat Nav directions                            |
| Slug:      | sat-nav-directions                            |
| Rank:      | 5 kyu                       |
| URL:       | [https://www.codewars.com/kata/5a9b4d104a6b341b42000070](https://www.codewars.com/kata/5a9b4d104a6b341b42000070)                 |
| Languages: |  `java`  `javascript`  `python`  `csharp`  |

---
## Description

# <span style='color:orange'>Background</span>

It is the middle of the night.

You are jet-lagged from your long cartesian plane trip, and find yourself in a rental car office in an unfamiliar city.

You have no idea how to get to your hotel. 

Oh, and it's raining. 

Could you be any more miserable?

But the friendly rental-car dude behind the desk says not to worry! He kindly pre-programs the car **Sat Nav** system with your destination. He smiles and assures you that the device works OK. What excellent service! What a nice man! 

Maybe things are not so bad after all.

Then he sniggers...


# <span style='color:orange'>City streets</span>

The city extends as far as the eye can see in all directions, and is laid out as a giant grid where all blocks are `1km` across.

Notice that [x,y] coordinates are described with units of `100m`

<img src="https://i.imgur.com/6MFbhPO.png" title="satnav city streets" />


# <span style='color:orange'>Kata task</span>

Your starting point is `[0,0]`

Simply follow the Sat Nav directions!

When you arrive at the destination return the final [x,y] coordinates.

# <span style='color:orange'>Sat Nav directions</span>

The device gives directions as text messages:

<span style='color:red'>*The first message*</span>
* `Head <NORTH,EAST,SOUTH,WEST>`
 
<span style='color:red'>*The en-route messages*</span>
* `Take the <NEXT,2nd,3rd,4th,5th> <LEFT,RIGHT>`
* `Go straight on for <100,200,300,...,900>m`
* `Go straight on for <1.0,1.1,1.2,...,5.0>km`
* `Turn around!`

<span style='color:red'>*The last message*</span>
* `You have reached your destination!`

<span style='color:orange'>NOTES</span>
* First and last messages are always present
* There may be any number of *en-route* messages
* Messages are always formatted corrrectly
* A `NEXT` turn message means you must to proceed to the *next* cross-street even if you are currently at an intersection
* But `Turn around` does not need to be done at an intersection. Just do a U-turn wherever you are!


<br/><br/>


<span style='color:gray'>Good Luck!<br/>DM</span>



---
