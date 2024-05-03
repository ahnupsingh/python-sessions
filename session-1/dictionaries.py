# Dictionaries

mustang = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

i7 = {
  "brand": "BMW",
  "model": "i7",
  "year": 1965
}

x = {
  "brand": "Tesla",
  "model": "X",
  "year": 2020
}

cars= {
  "mustang": mustang,
  "i7": i7,
  "x": x
}
print("+++++", cars)

# {
#   'mustang': {
#     'brand': 'Ford', 
#     'model': 'Mustang', 
#     'year': 1964
#   }, 
#   'i7': {
#       'brand': 'BMW', 
#       'model': 'i7', 
#       'year': 1965
#   }, 
#   'x': {
#       'brand': 'Tesla', 
#       'model': 'X', 
#       'year': 2020
#   }
# }

# new_cars = {
#     "mustang_brand": "Ford", "mustang_model": "Mustang", "mustang_year": 1964, "i7_brand": "BMW", .....
# }













# Dictionaries functions
print("Mustang Brand: ", mustang.get("brand"))
print("Car Properties: ", mustang.keys())
print("Mustang Specs: ", mustang.values())

mustang.update({"year": 2024})
print("Mustang set year to 2024: ", mustang)


print("\n---------")
# mustang["type"] = "Automatic"
mustang.update({"types": "Automatic"})
print("mustang updated", mustang)


print("\n---------")

mustang.setdefault("type", "automatic")
print("Set type of Mustang ", mustang)


count = {}
count["1"] = count.get("1", 0) + 1
print(count)

























# Iteration
for key, value in mustang.items():
    print(key, value)

for k, v in cars.items():
    print(k, v)

# Type conversion
print("----> ", list(cars))

mustang_arr = [("brand", "Ford"), ("model", "Mustang"), ("year", 1964)]
print(dict(mustang_arr))
mustang_arr.extend({"type", "automatic"})
print("Mustang array extended", mustang_arr)


























# WAP to flatten a dict
print(cars)

result = {}
for brand, details in cars.items():
    if (type(details) == dict):
      for specs, value in details.items():
          result[f"{brand}_{specs}"] = value

print(result)


# code readability