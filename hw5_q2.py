"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q2
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

#without using islower, isupper, lower, upper... Convert to lowercase!

converted_str = "";
num_changes = 0;

in_string = input("Please Enter a String: ");

for character in in_string:
    chr_ord = ord(character); #converts to a number
    if chr_ord >= 65 and chr_ord <= 90: #if within range of capital letters
        converted_str += chr(chr_ord + 32); #adding 32 makes it lowercase ASCII, and chr() changes it back into a regular character (not a number)
        num_changes += 1;
    else:
        converted_str += chr(chr_ord);

print(converted_str);
print("Number of changes:", num_changes);