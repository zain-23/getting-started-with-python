people = [
    {"name":"Zain","age":12},
    {"name":"Ali","age":32},
    {"name":"Hasin","age":24}
]
people.sort(key = lambda person:person["age"])
print(people)