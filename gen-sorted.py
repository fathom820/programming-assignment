#!/usr/bin/env python3

from __future__ import print_function
import time
import shared as s

start_time = time.time()
s.print_notif("begin sorted generation")

# open file
for i in range(3):
    read_dir        = s.const.unsorted_paths[i]
    lo_hi_dir       = s.const.lo_hi_paths[i]
    hi_lo_dir       = s.const.hi_lo_paths[i]
    current_size    = s.const.sizes[i]

    
    for j in range(s.const.num_files):
        read_from       = read_dir + str(j) + s.const.ext
        writeto_lo_hi   = lo_hi_dir + str(j) + s.const.ext
        writeto_hi_lo   = hi_lo_dir + str(j) + s.const.ext
        start           = time.time()
        numbers = s.file_to_array(read_from)

        numbers.sort()
        
        f = open(writeto_lo_hi, "w")
        for num in numbers:
            f.write(str(num) + "\n")
            
        f.close()
        s.print_action("sort lo-hi", writeto_lo_hi, start, True)

        numbers.reverse() # invert array
        f = open(writeto_hi_lo, "w")
        for num in numbers:
            f.write(str(num) + "\n")
        f.close()
        s.print_action("sort hi-lo", writeto_hi_lo, start, True)
        
    print("")

s.print_notif("done")
elapsed_time = format((time.time() - start_time), ",")
print("Total sorting time: " + elapsed_time[0:5] + " seconds")


