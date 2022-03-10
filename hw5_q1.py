"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q1
Date due: 2022-03-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
upper_count = 0;
lower_count = 0;
digit_count = 0;
other_count = 0;
invalid_count = 0;
pass_invalid = True;

password = input("Please enter a password: ");

if len(password) >= 8:
    for character in password:
        if character.isalpha():
            if character.isupper():
                upper_count += 1;
            else:
                lower_count += 1;
        elif character.isdigit():
            digit_count += 1;
        elif character == "!" or character == "@" or character == "#" or character == "$":
            other_count += 1;
        else:
            pass_invalid = False;
            invalid_count += 1;
else:
    pass_invalid = False;

if upper_count < 2 or lower_count < 2 or digit_count < 1 or other_count < 1:
    pass_invalid =  False;

#print("upper:",upper_count,"lower:", lower_count,"numbers:", digit_count,"other:",other_count,"invalid chr:",invalid_count);
print(pass_invalid);





