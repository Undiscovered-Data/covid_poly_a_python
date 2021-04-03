#!/usr/bin/python3

open_file = open('./dest/comp3.fasta', 'r')
writ_file = open('./dest/data.txt', 'w')


#Gets the Covid Name
def get_name(line):
    s_line = line.lstrip('>')
    a_list = s_line.split()
    the_name = a_list[0]
    return the_name
    
###########################################################################

#Takes the list and Covid Name and writes to data.txt
def process_it(inserted_list, inserted_name):
    poly_a_length = 0
    the_string = ''
    break_out = False
    while True:
        last_line = inserted_list.pop()
        s_line = last_line.strip()
        the_string = s_line + the_string
        for letter in the_string:
            if letter != 'A':
                break_out = True
                break
                
        if break_out:
            break
            
    flip_line = the_string[::-1]
    
    for letter in flip_line:
        if letter == 'A':
            poly_a_length += 1

        else:
            break
            
    writ_file.write(inserted_name)
    writ_file.write(": Poly_a_tail_length = ")
    
    the_tail_length = str(poly_a_length)
    
    writ_file.write(the_tail_length)
    writ_file.write('\n')

###########################################################################

the_list = []
first_line = True

for line in open_file:
    if first_line and line.startswith('>'):
        covid_name = get_name(line)
        first_line = False
        
    elif line.startswith('>'):
        process_it(the_list, covid_name)
        covid_name = get_name(line)
        the_list = []
        
    else:
        the_list.append(line)
        
#process the final list when end of file       
process_it(the_list, covid_name)


open_file.close()
writ_file.close()

