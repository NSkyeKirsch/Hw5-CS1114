"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q5
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
final_str = "";

in_string = input("Please enter an encoded string: ");
key = int(input("Enter a key: "));

for i in range(len(in_string)-1, -1, -key - 1):
    if(in_string[i].isdigit() == False):
        #print(in_string[i]);
        final_str += in_string[i];

print(final_str);

