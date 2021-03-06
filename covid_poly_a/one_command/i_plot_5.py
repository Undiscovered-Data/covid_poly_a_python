#!/usr/bin/python3

def plot_it(the_file):
    from collections import Counter
    import matplotlib.pyplot as plt
    
    print("\n\t\tPlotting\t5 of 5")

    open_file = open(the_file, 'r')

    the_list = []

    for line in open_file:
        s_line = line.strip()
        l_list = s_line.split()
        the_num = int(l_list[-1])
        the_list.append(the_num)

    the_count = Counter(the_list)

    the_max = max(the_list)

    max_plus_one = the_max + 1

    data_height = []
    data_number = []
    for the_number in range(1, max_plus_one):
        data_number.append(the_number)
        data_height.append(the_count[the_number])


    plt.bar(data_number, data_height, color='#098303')
    plt.show()

    open_file.close()

if __name__ == '__main__':
    plot_it('./dest/data.txt')
    
