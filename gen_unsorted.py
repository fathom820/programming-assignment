#!/usr/bin/env python
from __future__ import print_function

import os
import time
from random import randint

# track starting time of script for debugging purposes
start_time = time.time()

# ANSI color codes for formatted output; not all are used
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# generate directories if not found
# this is normally the case because run.sh removes any previous directories/files for cleanup purposes
def gen_dirs():
    paths = ["small/", "medium/", "large/"]
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

num_files = 30
ext = ".dat"
sizes = [10000, 100000, 1000000]
unsorted_paths = ["small/unsorted/", "medium/unsorted/", "large/unsorted/"]

gen_dirs() # create all necessary directories if they don't exist already

numbers_generated = 0
print(bcolors.HEADER + bcolors.BOLD + " -- BEGIN FILE GENERATION -- " + bcolors.ENDC)
for i in range(3):
    current_dir = unsorted_paths[i]
    current_size = sizes[i]
    
    for j in range(num_files):
        name = current_dir + str(j) + ext
        f = open(name, "w")
        file_start_time = time.time()
        for k in range(current_size):
            num = str(randint(0, 9999))
            f.write(num)
            f.write("\n")
            numbers_generated += 1
        f.close()
        file_end_time = time.time()
        file_elapsed_time = format((file_end_time - file_start_time), ",")

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

        print(bcolors.ENDC + bcolors.BOLD + bcolors.OKCYAN + "gen_unsorted" + bcolors.ENDC + " -> " + bcolors.OKGREEN + name + spacer + bcolors.OKCYAN + bcolors.BOLD + file_elapsed_time[0 : 4] + bcolors.ENDC + " seconds")

print(bcolors.BOLD + bcolors.HEADER + " -- DONE -- " + bcolors.ENDC)
elapsed_time = format((time.time() - start_time), ",")
numbers_generated = format(numbers_generated, ",")
print("Generated %s numbers across %d files in %s seconds" % (numbers_generated, (3 * num_files), elapsed_time[0:5]))