#!/usr/bin/python3

o_file = open("./dest/comp1.fasta", 'r')
wc_file = open("./dest/comp2.fasta", 'w')
wi_file = open("./dest/incomp2.fasta", 'w')

is_first = True
list_file = []
for line in o_file:
    if line.startswith('>') and is_first:
        list_file.append(line)
        is_first = False

    elif line.startswith('>'):
        if len(list_file) >= 400:
            for a in list_file:
                wc_file.write(a)
        else:
            for b in list_file:
                wi_file.write(b)

        list_file = []
        list_file.append(line)

    else:
        list_file.append(line)

if len(list_file) >= 400:
    for a in list_file:
        wc_file.write(a)
else:
    for b in list_file:
        wi_file.write(b)

o_file.close()
wc_file.close()
wi_file.close()

