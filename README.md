# Unit Testing 101

This repository is the code I wrote for my article [How to test a function?](https://davidfozo.com/blog/how-to-test-a-function)

It contains a python 3 module consisting of a function and the related unit tests.
The function's input is a string and the output is a dictionary of:
* the frequencies of the vowels each
* the frequency of all consonants total

The function checks for illegal inputs, raising TypeError if it is not a string. Also it does not count invalid characters like commas, ampersands and other symbols. Vowels and consonants are limited to the English language.


## Installation

Installation is simple. Clone the repo as you would usually do.
```
git clone https://github.com/fozodavid/UnitTesting101.git .
```

## Usage
```
>>> from vowelsCheck import vowelsCheck
>>> vowelsCheck("Hello World!")
{"e":1,"o":2,"consonants":7}
```

## Tests

Run the tests by:
```
python3 tests.py
```