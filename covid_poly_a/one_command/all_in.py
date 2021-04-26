#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sort_by_N_1
import too_short_2
import no_partial_3
import poly_a_tail_4
import i_plot_5

file_name = input("Enter the name of the file\nfor example Covid19.fasta  ")
keep_data_ques = input("Do you want to keep the processed files? Yes/No\nThey are big. If unsure type no:  ")
keep_data_l = keep_data_ques.strip().lower()[0]

if keep_data_l != 'y' and keep_data_l != 'n':
    raise Exception("You must enter yes or no.\Goodbye")
if keep_data_l == 'y':
    keep_data = True
else:
    keep_data = False

complete_num = sort_by_N_1.the_sort(file_name, keep_data)
complete_num2 = too_short_2.shorty('./dest/comp1.fasta', complete_num, keep_data)
complete_num3 = no_partial_3.nopartial("./dest/comp2.fasta", complete_num2, keep_data)
poly_a_tail_4.polya("./dest/comp3.fasta", complete_num3, keep_data)
i_plot_5.plot_it('./dest/data.txt')
