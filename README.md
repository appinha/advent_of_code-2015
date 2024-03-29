<h1 align="center">
	🌟 Advent of Code 2015 🎄
</h1>

<p align="center">
	<i>My solutions for <b>Advent of Code 2015</b>.</i>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/appinha/advent_of_code-2015?color=blueviolet" />
	<img alt="Number of lines of code" src="https://img.shields.io/tokei/lines/github/appinha/advent_of_code-2015?color=blueviolet" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/appinha/advent_of_code-2015?color=blue" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/appinha/advent_of_code-2015?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/appinha/advent_of_code-2015?color=brightgreen" />
</p>

<h3 align="center">
	<a href="#%EF%B8%8F-about">About</a>
	<span> · </span>
	<a href="#-what-is-advent-of-code">What is <i>Advent of Code</i>?</a>
	<span> · </span>
	<a href="#-contents">Contents</a>
	<span> · </span>
	<a href="#%EF%B8%8F-usage">Usage</a>
	<span> · </span>
	<a href="#%EF%B8%8F-table-of-puzzles">Table of puzzles</a>
</h3>

---

[![Day 01](https://badgen.net/badge/01/%E2%98%85%E2%98%85/yellow)](my_solutions/day01)
[![Day 02](https://badgen.net/badge/02/%E2%98%85%E2%98%85/yellow)](my_solutions/day02)
[![Day 03](https://badgen.net/badge/03/%E2%98%85%E2%98%85/yellow)](my_solutions/day03)
[![Day 04](https://badgen.net/badge/04/%E2%98%85%E2%98%85/yellow)](my_solutions/day04)
[![Day 05](https://badgen.net/badge/05/%E2%98%85%E2%98%85/yellow)](my_solutions/day05)
[![Day 06](https://badgen.net/badge/06/%E2%98%85%E2%98%85/yellow)](my_solutions/day06)
[![Day 07](https://badgen.net/badge/07/%E2%98%85%E2%98%85/yellow)](my_solutions/day07)
[![Day 08](https://badgen.net/badge/08/%E2%98%85%E2%98%85/yellow)](my_solutions/day08)
[![Day 09](https://badgen.net/badge/09/%E2%98%85%E2%98%85/yellow)](my_solutions/day09)
[![Day 10](https://badgen.net/badge/10/%E2%98%85%E2%98%85/yellow)](my_solutions/day10)
[![Day 11](https://badgen.net/badge/11/%E2%98%85%E2%98%85/yellow)](my_solutions/day11)
[![Day 12](https://badgen.net/badge/12/%E2%98%85%E2%98%85/yellow)](my_solutions/day12)
[![Day 13](https://badgen.net/badge/13/%E2%98%85%E2%98%85/yellow)](my_solutions/day13)
[![Day 14](https://badgen.net/badge/14/%E2%98%85%E2%98%85/yellow)](my_solutions/day14)

(TODO: add final picture of AoC calendar)

## 🗣️ About

(TODO: write)

## 🌟 What is *Advent of Code*?

	🚀 TLDR: an online event where a two-part programming puzzle is released each day from Dec 1st to the 25th.

[Advent of Code](http://adventofcode.com) is an online event created by [Eric Wastl](http://was.tl/). In his words:

> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

Source: https://adventofcode.com/about

### 🎄 This year story for the puzzles

> Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect **fifty stars** by December 25th.
>
>Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

## 📑 Contents

My solutions for the puzzles are available in the folder [📁 my_solutions](my_solutions) and are organized into subfolders for each day of the event.

Inside each subfolder, the following files can be found:

* `input_test.txt` - text file containing input from tests given in the puzzle.
* `input.txt` - text file containing my personal input for the puzzle.
* `main.py` - Python code for solving the puzzle.

## 🛠️ Usage

**Solve puzzle for a certain day:**

```
make day=01
```

**Solve puzzle for a certain day and part:**

```
make day=08 part=1
```

```
make day=08 part=2
```

**Solve puzzle for testing input:**

```
make test day=12
```

```
make test day=12 part=1
```

**Create a new day folder from template:**

```
make new day=02
```

## 🗓️ Table of puzzles

| DAY							| PUZZLE TITLE	| PUZZLE SUMMARY
| :-:							| :-						| :-
| [📁 01](my_solutions/day_01)	| **Not Quite Lisp**		| 📃 **Input:** a string of opening (up +1) and closing (down -1) parenthesis.<br />⭐ **Part One:** follow the directions (parenthesis) and find the right floor. <br />⭐ **Part Two:** find the position of the first character that causes entering the basement (floor -1).
| [📁 02](my_solutions/day_02)	| **I Was Told There Would Be No Math**		| 📃 **Input:** list of dimensions of present boxes.<br />⭐ **Part One:** find the total area of wrapping paper needed. <br />⭐ **Part Two:** find the total length of ribbon needed.
| [📁 03](my_solutions/day_03)	| **Perfectly Spherical Houses in a Vacuum**		| 📃 **Input:** a string of cardinal directions.<br />⭐ **Part One:** find how many houses receive at least one present. <br />⭐ **Part Two:** find how many houses receive at least one present.
| [📁 04](my_solutions/day_04)	| **The Ideal Stocking Stuffer**		| 📃 **Input:** a secret key.<br />⭐ **Part One:** find the lowest positive number (decimal) that, combined with the secret key, produces a MD5 hash that starts with five zeros. <br />⭐ **Part Two:** same as befor, but for six zeros.
| [📁 05](my_solutions/day_05)	| **Doesn't He Have Intern-Elves For This?**		| 📃 **Input:** a list of strings.<br />⭐ **Part One:** find how many strings are nice (according to given rules). <br />⭐ **Part Two:** same as before, but with different rules.
| [📁 06](my_solutions/day_06)	| **Probably a Fire Hazard**		| 📃 **Input:** instructions on how to display the ideal lighting configuration.<br />⭐ **Part One:** find how many lights are lit after following the instructions. <br />⭐ **Part Two:** find the total brightness of all lights combined after following the instructions.
| [📁 07](my_solutions/day_07)	| **Some Assembly Required**		| 📃 **Input:** instructions for assembling a circuit of wires and bitwise logic gates.<br />⭐ **Part One:** assemble the circuit by following the instructions to find signal provided to wire `a`. <br />⭐ **Part Two:** same as before, but overriding wire `b`'s signal with part one's answer.
| [📁 08](my_solutions/day_08)	| **Matchsticks**		| 📃 **Input:** a file that contains a list of double-quoted string literals.<br />⭐ **Part One:** find the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file. <br />⭐ **Part Two:** find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal.
| [📁 09](my_solutions/day_09)	| **All in a Single Night**		| 📃 **Input:** a list of distances between locations.<br />⭐ **Part One:** find the distance of the shortest route for visiting each location once. <br />⭐ **Part Two:** find the distance of the longest route for visiting each location once.
| [📁 10](my_solutions/day_10)	| **Elves Look, Elves Say**		| 📃 **Input:** a short sequence of digits.<br />⭐ **Part One:** starting with the digits from the puzzle input, apply the look-and-say sequence 40 times to find the length of the result. <br />⭐ **Part Two:** now for 50 times.
| [📁 11](my_solutions/day_11)	| **Corporate Policy**		| 📃 **Input:** a password (a string of 8 lowercase characters).<br />⭐ **Part One:** given Santa's method and Security-Elf requirements, find the next password. <br />⭐ **Part Two:** find the next password for the password found in part one.
| [📁 12](my_solutions/day_12)	| **JSAbacusFramework.io**		| 📃 **Input:** a json document containing arrays, objects, numbers, and strings.<br />⭐ **Part One:** find all of the numbers throughout the document and add them together. <br />⭐ **Part Two:** same as before, but ignoring any object (and all of its children) which has any property with the value "red".
| [📁 13](my_solutions/day_13)	| **Knights of the Dinner Table**		| 📃 **Input:** a guest list detailing the amount their happiness would increase or decrease depending on who sits next to them.<br />⭐ **Part One:** find the total change in happiness for the optimal seating arrangement, i.e. where maximum happiness is achieved. <br />⭐ **Part Two:** same as before, but adding a neutral guest to the table.
| [📁 14](my_solutions/day_14)	| **Reindeer Olympics**		| 📃 **Input:** descriptions of reindeers' flying patterns.<br />⭐ **Part One:** find what distance the winning reindeer traveled after 2503 seconds. <br />⭐ **Part Two:** find total points of winning reindeer after traveling for 2503 seconds.
<!--
| [📁 15](my_solutions/day_15)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 16](my_solutions/day_16)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 17](my_solutions/day_17)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 18](my_solutions/day_18)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 19](my_solutions/day_19)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 20](my_solutions/day_20)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 21](my_solutions/day_21)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 22](my_solutions/day_22)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 23](my_solutions/day_23)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 24](my_solutions/day_24)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
| [📁 25](my_solutions/day_25)	| **Title**		| 📃 **Input:** .<br />⭐ **Part One:** . <br />⭐ **Part Two:** .
 -->