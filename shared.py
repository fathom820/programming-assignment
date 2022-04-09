import time

# ANSI color codes for formatted output. Not all of them are used because I 
# copied this over from a previous project instead of bothering to
# look up all of the codes
class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

# constants that are shared across the various generator & sorting files
class const:
    num_files       = 30                                                            # number of files generated per category
    ext             = ".dat"                                                        # file extension for data files
    sizes           = [10000, 100000, 1000000]                                      # sizes of each data set
    input_paths     = ["input/small/", "input/medium/", "input/large/"]             # paths to all input directories
    input_dirs      = ["unsorted/", "small-large/", "large-small/"]                 # paths to each category in the path directories specified above
    unsorted_paths  = [                                                             # paths to each unsorted directory
        input_paths[0] + input_dirs[0],
        input_paths[1] + input_dirs[0],
        input_paths[2] + input_dirs[0]
    ]
    lo_hi_paths     = [                                                             # paths to each small-large directory
        input_paths[0] + input_dirs[1],
        input_paths[1] + input_dirs[1],
        input_paths[2] + input_dirs[1]
    ]
    hi_lo_paths     = [                                                             # paths to each large-small directory
        input_paths[0] + input_dirs[2],
        input_paths[1] + input_dirs[2],
        input_paths[2] + input_dirs[2]
    ]

    
# -------------------------------- #
#      miscellaneous functions     #
# -------------------------------- #

# prints confirmation that an action was performed on a certain file,
# along with how long it took. Mainly exists so that the user
# can tell the computer is actually doing work, but I've also used
# it for debugging.
def print_action(action, file_name, start_time):
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
    print(
        bcolors.ENDC + bcolors.BOLD + bcolors.OKCYAN + action + bcolors.ENDC + 
        " -> " + bcolors.OKGREEN + file_name + 
        spacer + 
        bcolors.OKCYAN + bcolors.BOLD + 
        file_elapsed_time[0 : 4] + bcolors.ENDC + " seconds"
    )

def print_notif(msg):
    print(bcolors.HEADER + bcolors.BOLD + " -- " + msg.upper() + " -- " + bcolors.ENDC)