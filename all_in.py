#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sort_by_N_1
import too_short_2
import no_partial_3
import poly_a_tail_4
import i_plot_5

file_name = input("Enter the name of the file\nfor example Covid19.fasta  ")
complete_num = sort_by_N_1.the_sort(file_name)
complete_num2 = too_short_2.shorty('./dest/comp1.fasta', complete_num)
complete_num3 = no_partial_3.nopartial("./dest/comp2.fasta", complete_num2)
poly_a_tail_4.polya("./dest/comp3.fasta", complete_num3)
i_plot_5.plot_it('./dest/data.txt')
