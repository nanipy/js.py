from js.core import console, require, Array

this = require("random");

nums = Array();
nums.length = 10;
nums.fill("Foobar");
console.log(nums);
