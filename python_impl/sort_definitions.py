def load_definitions(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    definitions = [line.strip() for line in lines if line.strip() != ""]
    return definitions

definitions = load_definitions("../data/definitions.txt")

memorized = ["Stack", "Queue"]

non_mem = []
mem = []

for d in definitions:
    if d in memorized:
        mem.append(d)
    else:
        non_mem.append(d)

non_mem.sort()

final_list = non_mem + mem

print("Final sorted list:")
for d in final_list:
    print(d)
