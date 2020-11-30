# aoc

These are my Advent of Code solutions. I use my
[aoc-cli](https://github.com/skeate/aoc-cli) tool to organize and run them.

## running

`./aoc -y <year> -d <day> -l <lang> run` will run the solution for the given
year, day, and language.

## structure

This project is really meant to be a starting point, so it's very flexible. Do
whatever you want with it. That said, the initial structure is as follows:

* `inputs` - problem inputs
* `solutions/<language>` - contains the solution code in the given language, as
    well as any runner or library code for that language.
* `templates` - contains the templates referenced in `config.yml`.
