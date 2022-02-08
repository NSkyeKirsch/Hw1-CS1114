"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q3
Date due: 2022-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter number of coins:");

quarters_input = int(input("# of quarters: "));
dimes_input = int(input("# of dimes: "));
nickels_input = int(input("# of nickels: "));
pennies_input = int(input("# of pennies: "));

num_total_dollars = quarters_input//4;
num_total_cents = (quarters_input%4) * 25;

num_total_dollars += (dimes_input//10);
num_total_cents += ((dimes_input%10) * 10);


num_total_dollars += (nickels_input//20);
num_total_cents += ((nickels_input%20) * 5);


num_total_dollars += (pennies_input//100);
num_total_cents += (pennies_input%100);

num_total_dollars += (num_total_cents//100);
num_total_cents = (num_total_cents%100);

print("The total is",num_total_dollars,"dollars and",num_total_cents,"cents");


