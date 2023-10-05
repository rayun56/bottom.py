# bottom.py

An implementation of [bottom](https://github.com/bottom-software-foundation/spec) in Python. Only the standard python
library is used.

## Usage

`python bottom.py encode "Hello!"`

`python bottom.py decode "💖✨✨,,👉👈💖💖,👉👈💖💖🥺,,,👉👈💖💖🥺,,,👉👈💖💖✨,👉👈✨✨✨,,,👉👈"`

You can also read input from a file:

`python bottom.py infile -o "bottom.txt" "string.txt"`

`python bottom.py outfile -o "string.txt" "bottom.txt"`

URLs are also supported:

`python bottom.py infile -o "out.txt" "https://www.o-bible.com/download/kjv.txt"`