#!/usr/bin/env python
from __future__ import print_function

import os
import time
import shared as s
from random import randint

# track starting time of script for debugging purposes
start_time = time.time()



# generate directories if not found
# this is normally the case because run.sh removes any previous directories/files for cleanup purposes
def gen_dirs():
    paths = ["input/small/", "input/medium/", "input/large/"]
    dirs = ["unsorted/", "small-large/", "large-small/"]

    # iteratively generate all needd folders
    for p in paths:
        for d in dirs:
            full_path = p + d
            if not os.path.isdir(full_path):
                print("Path " + full_path + " not found, creating")
                os.makedirs(full_path)
            else:
                print("Path " + full_path + " found, ignoring")

# todo: create function for printing file confirmation that takes filename + beginning execution time as input

num_files = 30
ext = ".dat"
sizes = [10000, 100000, 1000000]
unsorted_paths = ["input/small/unsorted/", "input/medium/unsorted/", "input/large/unsorted/"]

gen_dirs() # create all necessary directories if they don't exist already

numbers_generated = 0
print(s.bcolors.HEADER + s.bcolors.BOLD + " -- BEGIN FILE GENERATION -- " + s.bcolors.ENDC)
for i in range(3):
    current_dir = unsorted_paths[i]
    current_size = sizes[i]
    
    for j in range(num_files):
        name = current_dir + str(j) + ext
        f = open(name, "w")
        file_start_time = time.time()
        for k in range(current_size):
            num = str(randint(0, 10000))
            f.write(num)
            f.write("\n")
            numbers_generated += 1
        f.close()
        file_end_time = time.time()
        file_elapsed_time = format((file_end_time - file_start_time), ",")

        # makes it so that the time display is lined up,
        # regardless of how many characters came before it.
        # it wouldn't be my code if there wasn't my share of nitpicks.
        spacer = ""
        if i == 0 or i == 2:
            if j < 10:
                spacer = "     " # 5
            else:
                spacer = "    " # 4
        if i == 1:
            if j < 10:
                spacer = "    " # 4
            else:
                spacer = "   " # 3

        print(
            s.bcolors.ENDC + s.bcolors.BOLD + s.bcolors.OKCYAN + "gen" + s.bcolors.ENDC + 
            " -> " + s.bcolors.OKGREEN + name + 
            spacer + 
            s.bcolors.OKCYAN + s.bcolors.BOLD + 
            file_elapsed_time[0 : 4] + s.bcolors.ENDC + " seconds"
            )
    print("") # empty line as separator

print(s.bcolors.BOLD + s.bcolors.HEADER + " -- DONE -- " + s.bcolors.ENDC)
elapsed_time = format((time.time() - start_time), ",")
numbers_generated = format(numbers_generated, ",")
print("Generated %s numbers across %d files in %s seconds" % (numbers_generated, (3 * num_files), elapsed_time[0:5]))