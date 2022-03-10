"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q4
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
descending = True;
saved_letter = 100000;

in_string = input("Please enter aa string of lowercase letters: ");

for letter in in_string:
    if ord(letter) >= saved_letter:
        descending = False;
    saved_letter = ord(letter);

if(descending == False):
    print(in_string, "is not decreasing.");
else:
    print(in_string, "is decreasing.");
