#!/usr/bin/env python

from __future__ import print_function

import os
import time
import shared as s
from random import randint


start_time = time.time()

# generate directories if not found
# this is normally the case because run.sh removes any previous directories/files for cleanup purposes
def gen_dirs():
    # iteratively generate all needd folders
    for p in s.const.input_paths:
        for d in s.const.input_dirs:
            full_path = p + d
            if not os.path.isdir(full_path):
                print("Path " + full_path + " not found, creating")
                os.makedirs(full_path)
            else:
                print("Path " + full_path + " found, ignoring")


# back to main script

gen_dirs() # create all necessary directories if they don't exist already
numbers_generated = 0
s.print_notif("begin unsorted generation")

for i in range(3):
    current_dir     = s.const.unsorted_paths[i]
    current_size    = s.const.sizes[i]
    
    for j in range(s.const.num_files):
        name    = current_dir + str(j) + s.const.ext
        f       = open(name, "w")
        start   = time.time()

        for k in range(current_size):
            num = randint(0, 10000)
            f.write(str(num) + "\n")
            numbers_generated += 1
        
        f.close()
        
        s.print_action("generate file", name, start)

s.print_notif("done")
elapsed_time        = format((time.time() - start_time), ",")
numbers_generated   = format(numbers_generated, ",")
print("\bGenerated %s numbers across %d files in %s seconds" % (numbers_generated, (3 * s.const.num_files), elapsed_time[0:5]))