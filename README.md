# js.py
A library that extends Python base classes with their JavaScript default methods.

## Installation
`pip3 install js.py` or `pip3 install --user js.py`

## Why js.py?
js.py makes your JavaScript code compatible in Python with minor changes.

Imagine this JS code:
```js
var this = require("a-lib");

var nums = [];
nums.length = 10;
nums.fill("Foobar");
console.log(nums);
```

Using js.py, it looks like this:
```py
import js

this = require("a-lib");

nums = [];
nums.length = 10;
nums.fill("Foobar");
console.log(nums);
```

As seen above, only minor changes are required for the code for it to function in Python.

## Is it pythonic?
No. Not at all. But who cares? It works and it's for fun!
