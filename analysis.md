# analysis.md — Sorting Definitions with Memorized Terms Last

# 1. Problem Summary 
The assignment requires sorting textbook definitions in lexicographic order.  
However, the sorting algorithm must be designed to ignore definitions that are already memorized during the main sorting step, so that memorized definitions appear **after** the main sorted results.

In other words, the final output must be:

1) Non-memorized definitions sorted lexicographically by TERM  
2) Memorized definitions listed at the end not mixed into the sorted part

#2. Input / Output Design

# Inputs
  `data/cleaned_definitions.txt`  
A cleaned version of the dataset (definitions only, no blank lines / headings). This reduces the chance of errors and makes sorting predictable.

  `data/memorized.txt`  
  A separate file containing memorized **terms** (one term per line). Example terms:
  - Gaussian Elimination
  - Problem Reduction
  - Full Binary Tree
  - Internal Nodes
  - Hash function
  - Distance Matrix

# Output
`data/sorted_definitions.txt`  
The program writes the final sorted list into this file. This makes it easy for the grader to verify the result directly in the repository, without needing to re-run the code.

The program also prints a small preview (first 10 lines) and counts (non-memorized / memorized / total) to make testing and debugging easier.

# 3. Dataset Handling and Cleaning Choices
The dataset originally had extra content such as headings (e.g: “Chapter …”) and blank lines.  
These lines do not represent definitions and should not be sorted with real definitions.

To avoid sorting invalid lines, the program filters the dataset and keeps only definition entries that follow the expected format:

- Valid definition line format:
  `* **TERM**: definition...`

Filtering rule used in code:
- Only keep lines starting with: `* **`

This guarantees that headings (which start with `###`) and other non-definition lines are not included in sorting.

# 4. Algorithm Approach (High-level)
The algorithm uses a **two-list approach**:

- **List A**: non-memorized definitions  
- **List B**: memorized definitions
  
Steps:
1. Load all definition lines from `cleaned_definitions.txt`
2. Filter to keep only lines starting with `* **`
3. Load memorized terms from `memorized.txt` into a set (case-insensitive)
4. For each definition line:
   - Extract the TERM from `* **TERM**: ...`
   - If TERM is in memorized set → add to List B
   - Else → add to List A
5. Sort **only List A** lexicographically by TERM
6. Output = `List A + List B`
7. Write the final output to `sorted_definitions.txt`

This directly matches the requirement:  
“ignore memorized terms so they are listed after the main sorted results.”

# 5. TERM Extraction Method
To sort correctly, the program extracts the TERM from each definition line.

Example:
- Input line: `* **DFA**: Deterministic finite automaton.`
- Extracted term: `DFA`

The extraction works by:
- Confirming the line starts with `* **`
- Finding the closing `**`
- Slicing out the substring between them

This is more accurate than sorting by the entire line because sorting must be based on the term, not the definition text.

# 6. Time and Space Complexity

Let:
- `n` = number of definitions
- `m` = number of memorized terms
- `L` = average length of a definition line

# Loading input
- Reading files is O(n·L) overall (based on file size).

# Splitting into two lists
- For each definition, we extract the term and check membership in a set:
  - Extraction is O(L)
  - Set membership is O(1) average
- Total: O(n·L)

# Sorting
- We sort only the non-memorized definitions.
- Worst case (if none are memorized): sorting `n` items → O(n log n)
- Key extraction per comparison contributes O(L), so overall sorting cost is approximately:
  - O(n log n · L)

# Space
- Store definitions in memory: O(n·L)
- Memorized set: O(m)

# 7. Testing and Validation

# Goal of tests
The tests were designed to confirm:
1. Correct lexicographic sorting by TERM
2. Memorized terms are excluded from main sort and placed at the end
3. Headings / non-definition lines are ignored

# Test Case 1 — Basic sorting + memorized moved to end
Our Goal is - Check that non-memorized terms are sorted A→Z, and memorized terms are moved to the bottom.

memorized.txt:
NFA

Our Input definitions:
* **NFA**: nondeterministic finite automaton
* **DFA**: deterministic finite automaton
* **Alphabet**: set of symbols

Our Expected Output:
* **Alphabet**: set of symbols
* **DFA**: deterministic finite automaton
* **NFA**: nondeterministic finite automaton

# Test Case 2 - Ignore headings / non-definition lines
Our Goal is - Make sure headings like ### Chapter don’t appear in output only lines starting with * ** should be processed.

memorized.txt
CFG

Our Input definitions:
* **DFA**: deterministic finite automaton
* **CFG**: context-free grammar

Our Expected definitions:
* **DFA**: deterministic finite automaton
* **CFG**: context-free grammar

# Test Case 3 — All memorized
Our Goal is - if all terms are memorized, the main sorted results are empty and all output appears in the memorized section.

memorized.txt-
A
B

Our Input definitions:
* **B**: second
* **A**: first

Our Expected definitions:
* **A**: first
* **B**: second

# Final checks on real dataset
After running the script, I verified:
- No heading lines like `### Chapter` appear in the output file
- Non-memorized items appear sorted by TERM
- Memorized terms appear near the bottom of `sorted_definitions.txt`
- The script prints counts (Non-memorized + Memorized = Total)

# 8. Why a separate `memorized.txt` file was chosen
Instead of editing the dataset to add tags (e.g., `[MEM]`), the memorized list was stored separately because:
- It keeps the definition dataset clean and reusable
- Memorized terms can be updated without changing the dataset file
- It is easier to maintain and test different memorized lists
- It matches the idea of “later purposes” (reusing the same dataset with different memorized terms)

# 9. Conclusion
The final program satisfies the assignment requirements by:
- Sorting definitions lexicographically by TERM
- Separating memorized terms into a second list that is appended after the sorted results
- Producing a clear output file (`sorted_definitions.txt`) for easy verification
- Using filtering to ensure only real definition lines are processed


