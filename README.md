# GamblersGame

The problem from [Richard S. Sutton and Andrew G. Barto](http://incompleteideas.net/book/ebook/the-book.html), which can be solved using value iteration.

## Problem statement

A gambler has the opportunity to make bets on the outcomes of a sequence of coin flips. 
If the coin comes up heads, he wins as many dollars as he has staked on that flip; if it is tails, he loses his stake. The game ends 
when the gambler wins by reaching his goal of \$ 100, or loses by running out of money.
On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars.
