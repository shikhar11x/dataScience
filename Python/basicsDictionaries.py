Student={
    "name":"shikhar",
    "city":"ggn",
    "org":"msil"
}

print(Student)
print(Student["org"])
print(Student.get("name"))
print(Student.popitem())
del Student["city"]
print(Student)

Student={
    "name":"shikhar",
    "city":"ggn",
    "org":"msil"
}
print(Student.keys())
print(Student.values())
