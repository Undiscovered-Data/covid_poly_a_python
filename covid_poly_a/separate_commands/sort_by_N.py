#!/usr/bin/python3

the_file = input("Enter the file name e.g. Covid55.fasta   ")
o_file = open(the_file, 'r')
c_file = open('./dest/comp1.fasta', 'w')
i_file = open('./dest/incomp1.fasta', 'w')

is_first = True
the_list = []
has_N = False

for line in o_file:
    if is_first and line.startswith('>'):
        the_list.append(line)
        is_first = False
        
    elif line.startswith('>'):
        if has_N:
            for a in the_list:
                i_file.write(a)
            
            has_N = False
            the_list = []
            the_list.append(line)
            
        else:
            for a in the_list:
                c_file.write(a)

            has_N = False                
            the_list = []
            the_list.append(line)
            
    else:
        if 'N' in line:
            has_N = True

        the_list.append(line)

if has_N:
    for a in the_list:
        i_file.write(a)
                     
else:
    for a in the_list:
        c_file.write(a)

o_file.close()
c_file.close()
i_file.close()

