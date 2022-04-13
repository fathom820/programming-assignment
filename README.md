<center> 
<h1><u>Programming Assignment </u></h1>

Michael Frank <br>
CSC 310 <br>
Spring 2022 
</center>



# Info

This project compares the results of three classic sorting algorithms: quick sort, heap sort, and merge sort. There are 90 files each algorithm runs in total, divided like so:
* 30 unsorted
* 30 pre-sorted lowest to highest
* 30 pre-sorted highest to lowest

This data is stored in `input/`. Respectively, the output of each algorithm is stored in `output/`. These two directories won't be generated until the first and second scripts have finished running, respectively.

The results file (raw data) is `results.csv`.

For my report on the data and overall findings, see `report.pdf`.
<br>
# Instructions
I've compiled the dozen or so steps needed to run this project into several bash scripts for ease of use. The instructions stated that this project must run on the lab computers, which run Linux, so the bash scripts should be able to run. (They work on my computer, which is running Ubuntu 18.04 on WSL.)

**To run the entire project at once, run `run.sh`**.

To run the two portions of `run.sh` independently to see what they do, follow these instructions:

1. To generate the needed directories and input files for this project, run `./gen-all.sh`.
   - This should take about a minute and a half on average.
2. Once this is done (it will notify you), run `./sort.sh`.
   - This will iterate through each algorithm for each file automatically. 
   - Thanks to quicksort's **terrible** worst-case efficiency, this part take *quite a while* to run, so feel free to grab some snacks or a coffee while waiting.

Once completed, you should be able to check out the `results.csv` for the algorithms' output log. 

The `results.csv` included with this project submission corresponds with the `results.tar.gz` archive. The latter contains all the input and output files from me running this project on my computer.

# Documentation
I'm including a small breakdown of my code, and what each file does.
- `gen-unsorted.py` generates the input directories as well as the unsorted input files
- `gen-sorted.py` uses Python's `sort()` function to generate pre-sorted datasets to test the algorithms with
- `shared.py` is a library containing global constants and miscellaneous functions that are used across all of these files
- `quicksort.py`, `mergesort.py`, & `heapsort.py` all contain implementations of the respective algorithms as well as helper functions used only by those algorithms
- `sort-all.py` runs all three sorting algorithms for each input file, and stores their output in `output/[size]/[data type]/[algorithm]/`. The names of these output files correspond with the input files of the same name (`0.dat` ... `29.dat`)
- `gen-all.sh` runs `clean.sh`and runs `gen-unsorted.py` and `gen-sorted.py`
- `sort.sh` flushes any previous output and runs `sort-all.sh`
- `clean.sh` flushes previous input files