#!/usr/bin/env python3

from __future__ import print_function
import time
import shared as s
import quicksort
import sys

# ! increase recursion limit -- this is necessary for large files to run
sys.setrecursionlimit(100000000) # far bigger than necessary, lol


# open file
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
            
            start_time  = time.time()  
            quicksort.quick_sort(input_array, 0, len(input_array) - 1) 
            
            s.array_to_file(input_array, write_to)
            s.print_action("quick sort", write_to, start_time, False)