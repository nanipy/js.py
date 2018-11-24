import js

c = js.Array([1, 2, 3, 4, 5])
print(c.reduceRight(lambda x, y: x * y))
