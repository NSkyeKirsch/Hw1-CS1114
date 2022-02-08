"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q4
Date due: 2020-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount in the format of dollars and cents in two separate lines");
d_input = int(input());
c_input = int(input());

c_total = (d_input*100) + c_input;

q_total = c_total//25; #quarters
c_total -= (q_total*25); #start subtracting until pennies

d_total = c_total//10; #dimes
c_total -= (d_total*10);

n_total = c_total//5; #nickels
c_total -= (n_total*5);

p_total = c_total; #pennies

print(d_input,"dollars and",c_input,"cents are:",q_total,"quarters",d_total,"dimes",n_total,"nickels and",p_total,"pennies");



