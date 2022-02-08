"""
Author: Noa Kirschbaum
Assignment / Part: HW1 - Q2
Date due: 2020-02-10
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
seconds_in_year = 31536000;
original_population = 330109174;

year_input = int(input("How many years in the future? "));

num_births = (year_input*seconds_in_year)//7;
num_deaths = (year_input*seconds_in_year)//13;
num_immigrants = (year_input*seconds_in_year)//35;

est_population = (num_births + num_immigrants - num_deaths) + original_population;

print("the estimated population in",year_input,"years is",est_population);

