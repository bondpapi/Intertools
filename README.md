# Itertools
A python program that helps maximize List combinations. 
Maximizing Sum of Squares Modulo M

This project solves the problem of maximizing the sum of squares of integers chosen from multiple lists, modulo a given value M.
The objective is to pick one element from each list such that the sum of their squares is maximized, and the result is calculated modulo M.


## Overview

Given K lists of integers, the task is to compute the maximum possible value of the expression:

​	
  *is an element chosen from the i-th list, and M is a given modulo value.*
  *The program finds the best possible selection of elements to maximize the result.*


## How it Works

1. Input:
    -The user provides the number of lists K and the modulo value M.

    -Each subsequent line contains a list of integers, from which exactly one integer is chosen.

2. Calculation:
    -For each possible combination of chosen integers, the sum of their squares is calculated.

    -The result is then reduced modulo M, and the program tracks the maximum such value.

3. Output:
    The program outputs the maximum value of S modulo M.


## Features

- Handles up to 7 lists and efficiently computes the result.
- Works for lists containing integers of large magnitude (up to 10^9).
- Implements an intuitive brute-force combinatorial approach to find the optimal solution.

### Getting Started

## Prerequisites
- Python 3.x must be installed on your system.

# Installation

1. Clone this repository to your local machine:

git clone https://github.com/bondpapi/intertools

2. Navigate to the project directory:

`cd intertools`

## Usage

# Input Format
- The first line contains two integers, `K (number of lists) and M (the modulo value).`

- Each of the next K lines contains:
    `N(the number of integers in the list), followed by N space-separated integers representing the elements of the list.`

# Output Format
The program outputs a single integer, representing the maximum value of S modulo M.

## Example

# Sample Input

`3 1000`

`2 5 4`

`3 7 8 9`

`5 5 7 8 9 10`

# Sample Output

`206`

