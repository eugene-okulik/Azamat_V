my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": [1, True, "car", 2.35, 10],
    "dict": {"maker": "bmw", "model": "550i", "color": "black", "year": "2010", "condition": "not broken"},
    "set": {3, False, "cat", 3.35, 20}
}
print(my_dict["tuple"][-1])

my_dict["list"].append("test")
my_dict["list"].pop(1)

my_dict["dict"]["I am a tuple"] = 6
del my_dict["dict"]["color"]

my_dict["set"].add("new element")
my_dict["set"].remove("cat")
print(my_dict)



