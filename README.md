# Expense Splitter for Shared Flats

**Topic:** SE307-91

## First version

This is the first small step of the project. It is a command-line program for adding shared flat expenses, listing them, and showing their total.

## Run

Requires Python 3.

```bash
python expense_splitter.py
```

## Current features

- Add an expense description and amount
- Show all expenses entered in the current run
- Calculate the total amount

The expenses are kept in memory, so they are cleared when the program closes. This version does not split the expenses between roommates yet.

## Next steps

- Add roommate names
- Split expenses between roommates
- Save expenses so they are available the next time the program runs
