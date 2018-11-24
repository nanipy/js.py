import js

c = js.Array([1, 2, 3, 4, 5])
print(c._from("123456", lambda x: int(x) / 2))
