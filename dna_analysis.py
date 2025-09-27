# Download chr1_GL383518v1_alt and gunzip the file.
# Task 1
# Read the file 
file_path = "/Informatics_573/chr1_GL383518v1_alt.fa"
sequence = [] # empty list to store sequence lines
for line in open(file_path):
    if not line.startswith('>'): # skip header lines
            sequence.append(line.strip())
    else:
      pass
# join the list to make a single string of the whole sequence
sequence = ''.join(sequence).upper()

#print("Length of sequence =", len(sequence))# cross-checking length of the sequence

# 10th letter in the sequence
print("10th base =", sequence[9])
# 758th letter in the sequence
print("758th base =" ,sequence[757])
        


# Reverse complement of the sequence
# Task 2
reverse_complement = ''
for base in sequence:
    if base not in 'ATCG':
        print("Invalid base found:", base) #error handling for invalid bases
        break
else:
    reverse_complement = sequence.translate(str.maketrans('ACGT','TGCA'))[::-1] # used in-built method to get reverse complement
    
    #print("Length of reverse complement =", len(reverse_complement)) # cross-checking length of the reverse complement sequence

# print the 79th letter in the reverse complement sequence
print("79th base in reverse complement =", reverse_complement[78])
# print the 500th letter through 800th letter in the reverse complement sequence
print("500th base to 800th base in reverse complement =", reverse_complement[499:801])


# Task 3 - Create a nested dictionary
def nucleotides_count_sequence(sequence,kb_interval= 1000):
    """
    Returns a nested dictionary where each key is the starting index of a kilobase,
    and the value is a dictionary with counts of 'A', 'C', 'G', 'T' in that segment.
    """
    nucleotide_counts = {}

    for i in range(0, len(sequence), kb_interval):
        kb_segment = sequence[i:i + kb_interval]
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for base in kb_segment:
            if base in counts:
                counts[base] += 1
            else:
                print(f"Warning: Invalid base '{base}' found at position {i + kb_segment.index(base)}")

        nucleotide_counts[i] = counts

    return nucleotide_counts

# Call the function
my_dict = nucleotides_count_sequence(sequence)

# Iterate over each kilobase starting index and print the nucleotide counts
for kb_start_position in range(0, len(sequence), 1000):
# Use the get method to retrieve counts safely, defaulting to an empty dictionary if not found
    print(f"Nucleotide counts in kilobase starting at {kb_start_position}: {my_dict.get(kb_start_position, {})}")
print("5000:" , my_dict.get(5000)) # Example output for kilobase starting at 5000


# To read the dictionary that is created in Task 3
# Task 4 
nt_counts = nucleotides_count_sequence(sequence) #nucleotide counts
#print(nt_counts)

# First 1000 bp counts
first_kb_dict = list(nt_counts.values())[0]  # first kb
#print(first_kb_dict)
first_kb_count = [first_kb_dict[b] for b in ['A','C','G','T']]
print("Nucleotide counts in the first 1000 base pairs:", first_kb_count)

# All kb counts as list of lists
all_kb_counts = []
for kb_dict in nt_counts.values():
    all_kb_counts.append([kb_dict[b] for b in ['A','C','G','T']])
print(all_kb_counts)

# Sum of each kilobase
sums = [sum(kb) for kb in all_kb_counts]
print("Sums of nucleotide counts for each kilobase:", sums)

# Expected sum
expected_sum = 1000

# Identify discrepancies
differences = [i for i, s in enumerate(sums) if s != expected_sum]
print("Kilobases with sums not equal to", expected_sum, ":", differences, "index in sums")

# Print the actual counts for the kilobases that are not 1000
print("\nActual counts for kilobases with sum != 1000: is")
for i in differences:
    print(f"Kilobase starting at {list(nt_counts.keys())[i]}: {all_kb_counts[i]} (sum={sums[i]})")


if differences:
    print("The differences are likely due to the last kilobase containing fewer than 1000 bases. Deviations from the expected value may indicate sequence truncation or anomalies in the input data.")
else:
    print("All kilobases have sums equal to", expected_sum)


## Answers

# What is the expected sum for each list?
# Ans : 1000

# Are there any lists whose sums are not equal to the expected value?
# Ans : yes, Kilobase starting at 182000: [155, 92, 80, 112] (sum=439)

# Provide a general explanation for the differences in your expected results and your observed results.
# Ans : The differences are likely due to the last kilobase containing fewer than 1000 bases. Deviations from the expected value may indicate sequence truncation or anomalies in the input data.
