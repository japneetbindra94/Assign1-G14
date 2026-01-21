# COMP 359 – Assignment 1 (Topic 14)

## Sorting Textbook Definitions with Memorized Terms Ignored

### Course

COMP 359 – Design & Analysis of Algorithms

### Topic

Sort the definitions from the textbook in lexicographic order, while ignoring the definitions already memorized so that they appear after the main sorted results.

---

## Project Overview

This project processes a collection of textbook definitions and sorts them lexicographically by term. Definitions marked as memorized are excluded from the main sort and are appended at the end of the final output. This simulates a realistic scenario where known concepts are deprioritized during review.

The solution is implemented in Python for simplicity and clarity when working with text-based data. The definitions dataset is based on the textbook *The Design & Analysis of Algorithms (3rd ed.)* by Anany Levitin.

---

## Folder Structure

```
.
├── python_impl/
│   └── sort_definitions.py
├── data/
│   ├── cleaned_definitions.txt
│   ├── memorized.txt
│   ├── definitions.txt
│   └── sorted_definitions.txt
├── analysis.md
└── README.md
```

---

## How the Algorithm Works

1. Definitions are read from a cleaned text file.
2. Each definition line is parsed to extract the term.
3. A separate list of memorized terms is loaded.
4. Definitions are split into two groups:

   * Non-memorized definitions
   * Memorized definitions
5. Only non-memorized definitions are sorted lexicographically by term.
6. Memorized definitions are appended at the end without sorting.
7. The final result is written to an output file and partially displayed in the terminal.

---

## How to Run the Code

1. Ensure Python 3 is installed.

2. Clone the repository or extract the submitted git bundle.

3. Open a terminal and navigate to the `python_impl` directory:

   `cd python_impl`

4. Make sure the following files exist inside the `data` folder:

   * `cleaned_definitions.txt`
   * `memorized.txt`

5. Run the script:

   `python3 sort_definitions.py`

6. Output will be generated in:

   * `data/sorted_definitions.txt`

A short summary and preview of the results will also be printed to the terminal.

---

## Testing

Testing was performed using a small subset of definitions and a manually created list of memorized terms. The output was verified to ensure:

* Non-memorized definitions are sorted correctly
* Memorized definitions always appear after the sorted list

---

## Collaboration and Contributions

This was a collaborative assignment completed by both group members using a shared Git repository with regular commits from each contributor.

**Japneet Kaur**

* Implemented the Python sorting algorithm
* Organized and cleaned the definitions dataset
* Created the project structure
* Wrote the README documentation and run instructions

**Jang Toor**

* Assisted with testing and validation of results
* Reviewed extracted definitions and memorized terms
* Contributed to analysis and documentation through commits

The full contribution history can be seen in the git commit log on the main branch.

---

## References

Levitin, A. (2012). *The Design & Analysis of Algorithms* (3rd ed.). Pearson.

Python Software Foundation. Python Language Reference, version 3.x. [https://www.python.org](https://www.python.org)

AI Assistance: ChatGPT was used for guidance and clarification during development. All algorithm design, implementation decisions, and final code were written and verified by the authors.
