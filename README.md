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

This data is stored in `input/`. Respectively, the output of each algorithm is stored in `output/`.

The runtime of each algorithm for each respective file is stored in `out.dat`. To see the same data in a human-readable format, see `results.csv`.

For my report on the data and overall findings, see `report.pdf`.
<br>
# Instructions
I've compiled the dozen or so steps needed to run this project into several bash scripts for ease of use. The instructions stated that this project must run on the lab computers, which run Linux, so the bash scripts should be able to run. (They work on my computer, which is running Ubuntu 18.04 on WSL.)

1. To generate the needed directories and input files for this project, run `./gen-all.sh`.
   - This should take about a minute and a half on average.
2. Once this is done (it will notify you), run `./sort.sh`.
   - This will iterate through each algorithm for each file automatically. 
   - This part take *quite a while* to run, so feel free to grab some snacks or a coffee while waiting.

Once completed, you should be able to check out the `out.dat` file for the raw output. `results.csv` was generated by myself manually, so it will not display the exact same data. However, it should display the same trends.