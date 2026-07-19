# python-fundamentals

Three small command-line projects I built while learning Python basics. 
Nothing fancy, the point was to actually use loops, functions, file 
handling and basic error handling instead of just reading about them.

## What's in here

**calculator_and_guessing_game/** — a CLI calculator and a number guessing 
game with a limited number of attempts. First real Python I wrote that 
doesn't crash when you feed it garbage input.

**todo_list_cli/** — add, remove, and mark tasks done from the terminal. 
Tasks are saved to a JSON file so they're still there next time you run it.

**password_generator/** — generates passwords with options for length and 
symbols (`python pwgen.py --length 16 --symbols`), and also scores an 
existing password and tells you why it's weak.

## Running any of them

Each one is standalone, no dependencies outside the standard library.

    python3 <folder_name>/main.py   # or pwgen.py for the password one

## Notes

These were my first Python projects, so the code is simple on purpose.
This repo is really a snapshot of the basics before moving on to the 
bigger projects in my other repos.