# The $n$ queens problem

This file contains an outline of the $n$ queens problem, and a list of
exploratory tasks for you to attempt. As a group, discuss which questions you
would like to explore, and use AI to try and provide some answers/insights.

## Problem setup

On a chessboard, we say that two queens can _see each other_ if they lie on the
same row, column or diagonal. For a positive integer, $n$, we say that an
_$n$-configuration_ is a placement of $n$ queens on an $n \times n$ chessboard.
An $n$-configuration such that no two queens can see each other is called
_valid_; otherwise, the $n$-configuration is _invalid_.

## Potential routes of exploration

1. What is the best way of displaying a configuration?
2. How many valid $n$-configurations are there in the following cases?
   1. $n = 2$
   2. $n = 6$
   3. $n = 10$
   4. Arbitrary $n$
3. Given an $n \times n$ chessboard with $k < n$ queens placed, is it possible
   to extend it to a valid $n$-configuration?
4. Given an $n \times n$ chessboard with $k < n^2$ squares removed, how many
   possible ways are there to extend it to a valid $n$-configuration?
