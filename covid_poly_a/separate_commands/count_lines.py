#!/usr/bin/python3

the_file = input("Enter the file name, e.g. Covid_19.fasta   ")
o_file = open(the_file, 'r')

line_number = 0
number_of_lines = 0
by_hundred = [0] * 6
for line in o_file:
    line_number += 1
    if ">" in line and number_of_lines == 0:
        virus_name = line
        continue
    elif ">" in line:
        if number_of_lines < 100:
            by_hundred[0] += 1
        elif number_of_lines < 200:
            by_hundred[1] += 1
        elif number_of_lines < 300:
            print(virus_name)
            print(line_number)
            by_hundred[2] += 1
        elif number_of_lines < 400:
            print(virus_name)
            print(line_number)
            by_hundred[3] += 1
        elif number_of_lines < 500:
            by_hundred[4] += 1
        elif number_of_lines < 600:
            by_hundred[5] += 1
        
        
        else:
            print("bigger")
            
        number_of_lines = 0
        virus_name = line
    else:
        number_of_lines += 1
        
o_file.close()
for a in by_hundred:
    print(a)

