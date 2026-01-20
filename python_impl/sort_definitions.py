def load_lines(filename):
    """Load non-empty lines from a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def extract_term(def_line):
    """ Extract TERM from: definitions """
    if not def_line.startswith("* **"):
        return None
    end = def_line.find("**", 4)
    if end == -1:
        return None
    return def_line[4:end].strip()

# Input Taken from the files
definitions = load_lines("../data/cleaned_definitions.txt")

# Filter out anything that is not a real definition line
definitions = [d for d in definitions if d.startswith("* **")]

memorized_terms = set(t.lower() for t in load_lines("../data/memorized.txt"))

# Split into List A which is non-memorized and List B which is memorized
non_mem = []
mem = []

#loop to extract terms
for d in definitions:
    term = extract_term(d)
    if term and term.lower() in memorized_terms:
        mem.append(d)
    else:
        non_mem.append(d)

# Sort only the non-memorized list lexicographically by TERM
non_mem.sort(key=lambda line: (extract_term(line) or "").lower())

# Final list: sorted non-memorized first, memorized last
final_list = non_mem + mem

# OUTPUT FILE 
out_file = "../data/sorted_definitions.txt"
with open(out_file, "w", encoding="utf-8") as f:
    for line in final_list:
        f.write(line + "\n")

# So Basically we are having the output file as well as Printing the result. Output file because easier to show the result during the Presentation
# PRINT
print(f"Wrote sorted output to: {out_file}")
print(f"Non-memorized: {len(non_mem)} | Memorized: {len(mem)} | Total: {len(final_list)}")
print("\nPreview (first 10 lines):")
for line in final_list[:10]:
    print(line)
