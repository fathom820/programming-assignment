#!/usr/bin/env python3

from __future__ import print_function
import time
from mergesort import merge_sort
import shared as s
import quicksort
import mergesort
import heapsort
import sys
import os

# ! increase recursion limit -- this is necessary for large files to run
sys.setrecursionlimit(100000000) # 1,000,000 -- far bigger than necessary, lol

s.init_results() # generate header in csv file

for i in range(3):
    for j in range(3):
        # input and output directories change
        input_dir       = s.const.input_paths[i] + s.const.dirs[j]
        output_dir      = s.const.output_paths[i] + s.const.dirs[j]
        
        # input and output files change
        for k in range(s.const.num_files):
            read_from   = input_dir + str(k) + s.const.ext
            write_to    = output_dir + str(k) + s.const.ext
            input_array = s.file_to_array(read_from)        
            
            # ! Quick Sort 
            start_time  = time.time()
            quicksort.quick_sort(input_array, 0, len(input_array) - 1)
            s.record_results("Quicksort", s.const.sizes_str[i], s.const.cases[j], start_time) # log results to results.csv
            dir_ = output_dir + "quicksort/"
            
            if not os.path.isdir(dir_):
                os.makedirs(dir_)
                
            write_to = dir_ + str(k) + s.const.ext
            s.array_to_file (input_array, write_to)
            s.print_action  ("Quicksort", write_to, start_time, False) # terminal feedback
            
            # ! Merge Sort
            # this is the only implementation that isn't in-place. 
            # i couldn't figure out a way to do it otherwise.
            start_time  = time.time()
            out = mergesort.merge_sort(input_array)
            s.record_results("Mergesort", s.const.sizes_str[i], s.const.cases[j], start_time) # log results to results.csv
            dir_ = output_dir + "mergesort/"
            
            if not os.path.isdir(dir_):
                os.makedirs(dir_)
                
            write_to = dir_ + str(k) + s.const.ext
            s.array_to_file(out, write_to)
            s.print_action("Mergesort", write_to, start_time, False)
            
            # ! Heap Sort
            start_time  = time.time()
            heapsort.heap_sort(input_array)
            s.record_results("Heapsort", s.const.sizes_str[i], s.const.cases[j], start_time)
            dir_ = output_dir + "heapsort/"
            
            if not os.path.isdir(dir_):
                os.makedirs(dir_)
                
            write_to = dir_ + str(k) + s.const.ext
            s.array_to_file(input_array, write_to)
            s.print_action("Heapsort ", write_to, start_time, False)
