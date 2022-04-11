"""
This is a common library with functions and variables that
are utilized by pretty much every single file in the project. 
Everything shared by different files is stored here,
with no particular arrangement.
"""

import time # measuring runtime
import csv  # writing to results.csv

# ANSI escape codes for formatted output. Not all of them are used because I 
# copied this over from a previous python project instead of bothering to
# look up every single one of those annoying codes again.
# ! some terminals may not render them properly.
class colors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

# constants that are shared across all files
class const:
    num_files           = 30                                                            # number of files generated per category
    ext                 = ".dat"                                                        # file extension for data files
    sizes               = [10000, 100000, 1000000]                                      # sizes of each data set
    results_file        = "results.csv"
    sizes_str           = ["Small", "Medium", "Large"]
    cases               = ["Unsorted", "Small to Large", "Large to Small"]
    input_paths         = ["input/small/", "input/medium/", "input/large/"]             # paths to all input directories
    dirs                = ["unsorted/", "small-large/", "large-small/"]                 # paths to each category in the path directories specified above
    output_paths        = ["output/small/", "output/medium/", "output/large/"]
    unsorted_paths      = [                                                             # paths to each unsorted directory
        input_paths[0]  + dirs[0],
        input_paths[1]  + dirs[0],
        input_paths[2]  + dirs[0]
    ]
    lo_hi_paths         = [                                                             # paths to each small-large directory
        input_paths[0]  + dirs[1],
        input_paths[1]  + dirs[1],
        input_paths[2]  + dirs[1]
    ]
    hi_lo_paths         = [                                                             # paths to each large-small directory
        input_paths[0]  + dirs[2],
        input_paths[1]  + dirs[2],
        input_paths[2]  + dirs[2]
    ]
    out_unsorted_paths  = [
        output_paths[0] + dirs[0],
        output_paths[1] + dirs[0],
        output_paths[2] + dirs[0]
    ]
    out_lo_hi_paths     = [
        output_paths[0] + dirs[1],
        output_paths[1] + dirs[1],
        output_paths[2] + dirs[1]
    ]
    out_hi_lo_paths     = [
        output_paths[0] + dirs[2],
        output_paths[1] + dirs[2],
        output_paths[2] + dirs[2]
    ]

    
# -------------------------------- #
#      miscellaneous functions     #
# -------------------------------- #

# prints confirmation that an action was performed on a certain file,
# along with how long it took. exists so that the user
# can tell that the computer is actually doing work.
def print_action(action, file_name, start_time, console_only):
    # makes it so that the time display is lined up,
    # regardless of how many characters came before it.
    # it wouldn't be my code if there wasn't my share of nitpicks.
    prespace_len    = len(action + " -> " + file_name)
    spacer          = ""
    lim             = 50

    # in case string preceding the runtime display is longer than default limiter,
    # move the limiter. This will do it in increments of 5, which will
    # look better than having it change for each different input length.
    while (lim - prespace_len < 1):
        lim += 5
    for i in range(0, lim - prespace_len):
        spacer += " "

    file_elapsed_time = format((time.time() - start_time), "")
    out = colors.ENDC + colors.BOLD + colors.OKCYAN + action + colors.ENDC + " -> " + colors.OKGREEN + file_name + spacer + colors.OKCYAN + colors.BOLD + file_elapsed_time[0 : 4] + colors.ENDC + " seconds"
    print(out)
    
    #if not console_only:
     #   f = open(const.results_file, "a")
      #  f.write(action + "-" + file_name + "-" + file_elapsed_time + "\n")
       # f.close()


# prints a formatted notification to the console
def print_notif(msg):
    print(colors.HEADER + colors.BOLD + " -- " + msg.upper() + " -- " + colors.ENDC)


# reads contents of a file, separated by line,
# then stores them in an array. Returns said array
def file_to_array(file):
    out = []
    f = open(file, "r")
    for line in f.readlines():
        out.append(int(line))
    f.close()
    return out
  
  
# writes every element in an array to a file,
# each on a separate line.
def array_to_file(A, file):
    f = open(file, "w")
    for num in A:
        f.write(str(num) + "\n")
    f.close()
    
# write out header in CSV file
def init_results():
    f = open(const.results_file, "w")
    writer = csv.writer(f)
    header = ["Action", "Size", "Case", "Runtime"]
    f.close()
    
# record results in CSV file
# action: sorting algorithm ("Quicksort", "Mergesort", "Heapsort")
# size: data size (10,000, 100,000, 1,000,000)
# time: starting time of algorithm
def record_results(action, size, case, time_):
    elapsed_time = time.time() - time_
    f = open(const.results_file, "a")
    writer = csv.writer(f)
    writer.writerow([action, size, case, elapsed_time])
    f.close()