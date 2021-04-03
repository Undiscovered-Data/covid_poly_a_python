#!/usr/bin/python3

o_file = open("./dest/comp2.fasta", 'r')
wc_file = open("./dest/comp3.fasta", 'w')
wi_file = open("./dest/incomp3.fasta", 'w')

is_first = True
is_partial = False
file_list = []
for line in o_file:
    if line.startswith(">") and is_first:
        if "partial" in line:
            is_partial = True

        file_list.append(line)
        is_first = False

    elif line.startswith(">"):
        if is_partial:
            for a in file_list:
                wi_file.write(a)
        else:
            for b in file_list:
                wc_file.write(b)

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
else:
    for b in file_list:
        wc_file.write(b)

o_file.close()
wc_file.close()
wi_file.close()

