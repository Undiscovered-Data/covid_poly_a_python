#!/usr/bin/python3

import your_bar

def shorty(the_file, compare_num):
    o_file = open(the_file, 'r')
    wc_file = open("./dest/comp2.fasta", 'w')
    wi_file = open("./dest/incomp2.fasta", 'w')

    print("\n   Removing Entries that are too short\n")
    your_bar.start_it()

    the_step = compare_num / 50
    the_count = 0
    long_enough = 0
    way_short = 0
    
    is_first = True
    list_file = []

    for line in o_file:
        if line.startswith(">") and is_first:
            list_file.append(line)
            is_first = False
            the_count += 1

        elif line.startswith(">"):
            if len(list_file) >= 400:
                for a in list_file:
                    wc_file.write(a)
                long_enough += 1
                
            else:
                for b in list_file:
                    wi_file.write(b)
                way_short += 1

            list_file = []
            list_file.append(line)
            the_count += 1
            if the_count > the_step:
                your_bar.add_star()
                the_count = 0

        else:
            list_file.append(line)

    if len(list_file) >= 400:
        for a in list_file:
            wc_file.write(a)
        long_enough += 1
        
    else:
        for b in list_file:
            wi_file.write(b)
        way_short += 1

    your_bar.end_it()

    o_file.close()
    wc_file.close()
    wi_file.close()
    
    print("\n\tLong enough {}".format(long_enough))
    print("\tToo short {}".format(way_short))
    
    return long_enough

