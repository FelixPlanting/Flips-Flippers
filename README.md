## Motivation

I was scrolling through Instagram reels and saw a fun little math thingy that I thought would be easy to turn
into a playable game. The implementation is simple and quickly made but it's a kinda neat puzzle I think.
The game itself explains how to play.

## Solution
I'd recommend giving it a try (probably with pen and paper)
before resorting to the solution, but it's definitely on the hard side of things,
so if you've given up, here's how you're supposed to solve it:

For the starting state, there are four possible options:
- All switches are turned off
- Two switches diagonally opposite from each other are turned off and the other two are turned on
- Two switches next to each other are turned on and the other two are turned off
- Only one switch is turned on

We're going to systematically eliminate these four possibilities. How fast you can reliably solve this puzzle therefore
does depend on the random starting state you get, but it never takes more than 15 steps if done correctly.

First, flip all the switches to eliminate the possibility they were all turned off.

Then, flip a diagonally opposite pair, followed by flipping all four switches again. This eliminates
the possibility that two diagonal opposites were turned on and the other two were turned off.

Since we now know that there aren't two diagonally matched pairs, we can get to seeing if there are two diagonally
mismatched pairs. Flip an adjacent pair to ensure that if this is the case, the pairs are now matched.
Flip all, then a pair, then all again.

If the bulb is still not on, it means only one pair is mismatched.
Flip any switch, then flip all four. You now either have two matched pairs or two mismatched pairs.
Flip all, then a pair, then all again to test for matched pairs.
If the bulb is still off, press two adjacent buttons to force the pairs to match, then do the same thing as before
by flipping all, then a pair, then all again. The bulb is now guaranteed to be on.

An example of what would always work is 1234 13 1234 12 1234 13 1234 1 1234 13 1234 12 1234 13 1234.

Kinda cool, right?
