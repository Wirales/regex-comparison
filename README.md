# Regex Comparison Program

## Overview
This Python program compares regular expressions by converting them into non-deterministic finite automata (NFA) and then deterministic finite automata (DFA). It checks for equivalence between two regular expressions and provides a counterexample if they are not equivalent.

## Features
- Compare two or more regular expressions to check if they describe the same language.
- Provides a counterexample if the regular expressions are not equivalent.
- Uses the `automata` library to handle NFA and DFA conversions.

## Example
```python
regex1 = "(b|ab)*"
regex2 = "((a|())bb*)*"
