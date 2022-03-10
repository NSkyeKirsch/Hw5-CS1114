"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q3
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

#make an alternating sequence
#if a mistake is found, do not include it
#take finished sequence and print its compliment
sequence = "";
complement_seq = "";
dna_one_fixed = "";
dna_two_fixed = "";
index_1 = 0;
index_2 = 0;

dna_one = input("Enter a DNA sequence: ");
dna_two = input("Enter a second DNA sequence: ");

for nucleotide in dna_one:
    #print("nucleotide:",nucleotide);
    if(nucleotide == "A" or nucleotide == "C" or nucleotide == "T" or nucleotide == "G"):
        dna_one_fixed += nucleotide;

#print(dna_one_fixed);

for nucleotide in dna_two:
    #print("nucleotide:",nucleotide);
    if(nucleotide == "A" or nucleotide == "C" or nucleotide == "T" or nucleotide == "G"):
        dna_two_fixed += nucleotide;

#print(dna_two_fixed);


countdown = len(dna_one_fixed) + len(dna_two_fixed);

for digit in range(countdown + (len(dna_one_fixed)-len(dna_two_fixed))):
    if(digit%2 == 0):
        if(index_1 < len(dna_one_fixed)):
            sequence += dna_one_fixed[index_1];
            index_1 += 1;
    else:
        if (index_2 < len(dna_two_fixed)):
            sequence += dna_two_fixed[index_2];
            index_2 += 1;

#print(sequence);

for n in sequence:
    if(n == "A"):
        complement_seq += "T";
    elif(n == "C"):
        complement_seq += "G";
    elif(n == "T"):
        complement_seq += "A";
    elif(n == "G"):
        complement_seq += "C";
    else:
        print("what happened????");

print(complement_seq);


