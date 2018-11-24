# js.py
A library that extends Python base classes with their JavaScript default methods.

## Why js.py?
js.py makes your JavaScript code compatible in Python.

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
from js import console, require, Array

this = require("a-lib");

nums = Array();
nums.length = 10;
nums.fill("Foobar");
console.log(nums);
```

It lets you use most of your JS code in Python with only minor changes!

## Is it pythonic?
No. Not at all? But who cares? It works and it's for fun!
