# DNA Sequence Analysis Python Basic

## Identifying Information

* **Name:** Jnana Deepthi Vishnumolakala
* **Programming Language:** Python 3.12
* **Date Submitted:** September 27, 2025
* **Purpose:**
  This script performs analyses on the DNA sequence of `chr1_GL383518v1_alt`, including:

  1. Reading the full sequence and retrieving specific nucleotides.
  2. Generating the reverse complement of the DNA sequence and retrieving specific subsequences.
  3. Counting nucleotide occurrences per kilobase and storing results in a nested dictionary.
  4. Summarizing counts in lists, calculating sums, and identifying kilobases with sums different from the expected value.

---

## Required Files

1. **`chr1_GL383518v1_alt.fa`** – FASTA file containing the DNA sequence.
2. **`dna_analysis.py`** – Python script containing the code.

---

## Instructions to Run the Script

1. Ensure that **Python 3.12** is installed on your machine.

2. Place the following files in the same directory:

   * `chr1_GL383518v1_alt.fa` – DNA sequence file.
   * `dna_analysis.py` – Python script for analysis.

3. **Option 1: Using Terminal / Command Prompt**

   * Open a terminal or command prompt in the directory containing the files.
   * Run the script using the command:

     ```bash
     python dna_analysis.py
     ```
   * The output will be printed in the terminal.

4. **Option 2: Using an IDE (PyCharm / VSCode / IDLE)**

   * Open your IDE and open the folder containing your script.
   * Open the file `dna_analysis.py`.
   * Run the script using the IDE’s **Run** button.
   * The output will appear in the IDE’s console.

---
## Observations

* The expected sum of nucleotides per kilobase is **1000**.
* Deviations from this expected value may indicate sequence truncation or anomalies in the input data.
