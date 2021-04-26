#!/usr/bin/python3

import os

def the_sort(the_file, keep_data):
    o_file = open(the_file, 'r')
    c_file = open('./dest/comp1.fasta', 'w')
    i_file = open('./dest/incomp1.fasta', 'w')

    is_first = True
    the_list = []
    has_N = False
    total_virus = 0
    count_virus = 0
    icount_virus = 0

    print("\n\tRemoving viruses with N\n")
    
    for line in o_file:
        if is_first and line.startswith('>'):
            the_list.append(line)
            is_first = False
            total_virus += 1

        elif line.startswith('>'):
            total_virus += 1
            if total_virus % 10000 == 0:
                print("\t{} units read".format(total_virus))
            if has_N:
                for a in the_list:
                    i_file.write(a)

                the_list = []
                the_list.append(line)
                icount_virus += 1
                has_N = False

            else:
                for a in the_list:
                    c_file.write(a)

                has_N = False
                the_list = []
                the_list.append(line)
                count_virus += 1

        else:
            if 'N' in line:
                has_N = True

            the_list.append(line)

    if has_N:
        for a in the_list:
            i_file.write(a)
        icount_virus += 1

    else:
        for a in the_list:
            c_file.write(a)
        count_virus += 1

    o_file.close()
    c_file.close()
    i_file.close()
    print("\n\tTotal {}".format(total_virus))
    print("\tComplete {}".format(count_virus))
    print("\tIncomplete {}".format(icount_virus))

    if not keep_data:
        os.remove('./dest/incomp1.fasta')

    return count_virus

if __name__ == "__main__":
    s_file = input("Enter the name of the file")
    the_sort(s_file)

    
