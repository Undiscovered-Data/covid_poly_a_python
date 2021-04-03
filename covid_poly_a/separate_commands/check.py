#!/usr/bin/python3

the_file = input("Enter the file name,\nfor example Covid_55.fasta   ")
the_count = 0
comp = open(the_file, 'r')
for line in comp:
    if '>' in line:
        the_count += 1
        if the_count % 10000 == 0:
            print("{} viruses so far...".format(the_count))
print(the_count)
comp.close()
