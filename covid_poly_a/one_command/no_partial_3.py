#!/usr/bin/python3
import sys

def nopartial(the_file, compare_num):
    o_file = open(the_file, 'r')
    wc_file = open("./dest/comp3.fasta", 'w')
    wi_file = open("./dest/incomp3.fasta", 'w')
    
    print("\n\tRemoving viruses with partial")
    print("\n  ***            Percent Complete                ***")
    print("  |                                                |")
    print("  0% ################## 50% ################### 100%")
    print("  |                                                |")
    sys.stdout.write("  ")
    sys.stdout.flush()

    a_step = compare_num / 50
    the_count = 0
    complete_files = 0
    incomplete_files = 0
    is_first = True
    is_partial = False
    file_list = []
    for line in o_file:
        if line.startswith(">") and is_first:
            if "partial" in line:
                is_partial = True

            file_list.append(line)
            is_first = False
            the_count += 1

        elif line.startswith(">"):
            if is_partial:
                for a in file_list:
                    wi_file.write(a)
                incomplete_files += 1
            else:
                for b in file_list:
                    wc_file.write(b)
                complete_files += 1
                    
            the_count += 1
            if the_count > a_step:
                sys.stdout.write("*")
                sys.stdout.flush()
                the_count = 0

            if "partial" in line:
                is_partial = True
            else:
                is_partial = False

            file_list = []
            file_list.append(line)

        else:
            file_list.append(line)

    if is_partial:
        for a in file_list:
            wi_file.write(a)
        incomplete_files += 1
    else:
        for b in file_list:
            wc_file.write(b)
        complete_files += 1

    sys.stdout.write('\n')
    sys.stdout.flush()
    o_file.close()
    wc_file.close()
    wi_file.close()
    
    print("\n\tComplete files {}".format(complete_files))
    print("\tIncomplete files {}".format(incomplete_files))
    
    return complete_files

