def load_defination(filename);
with open(filename, "r", encoding="utf-8") as file:

lines = file.readlines()
 definitions = [line.strip() for line in lines if line.strip() != ""]
    return definitions

definitions = load_definitions("../data/definitions.txt")

for d in definitions:
    print(d)


