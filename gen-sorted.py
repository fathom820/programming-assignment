#!/user/bin/env python

from __future__ import print_function
import time
import shared as s

# open file
for i in range(3):
    current_dir = s.const.unsorted_paths[i]
    current_size = s.const.sizes[i]

    

    for j in range(s.const.num_files):
        numbers = []
        name    = current_dir + str(j) + s.const.ext
        f       = open(name, "r")
        start   = time.time()

        for line in f.readlines():
            numbers.append(int(line))
        f.close()

        numbers.sort()
        # todo: write to sorted files

        s.print_action("sort hi-lo", name, start)