# RHUL PP Cluster Scripts

This repo contains a few scripts to help with running on the RHUL PP cluster.

## Queue management

`queue_management.py` contains two scripts to find out how many jobs are
currently running on the farm. The two functions are:
- `get_queue(queue_name="")` - this function returns a list containing
  the jobs running and queued in a given queue. It is essentially a python
  wrapper around `qstat`. The `queue_name` argument is the name of the queue or the
  username you wish you filter by. For example you may only want the jobs in the
  long queue, in which case you set `queue_name="long"`, or you may want to the jobs
  you are currently running, `queue_name="-u lwilkins"`. 
- `count_queue_numbers(queue, sum_output=False)` - this function takes as input
  the output of `get_queue` and returns the number of jobs running and queued in
  the queue you have specified. The `sum_output` bool ditctates whether the
  function returns a `tuple` with the two elements being the number of jobs running
  and the number queued or returns a single `int` which is the sum of both.

`drip_feed_example.py` uses the functions discussed above to show an example
script where 10000 jobs need to be submitted to the farm. Unfortunately the farm
cannot handle more than 4000 jobs in the queue at a given time so if you are
submitting many 000's of jobs, you need to add a mechanism to your submission
script which checks there are not too many jobs in the queue. This script walks
through a basic example of this.

## Example run script

`example_run_script.sh` is a simple example run script for submitting to the
farm. It contains all of the best practices including tracking the peak memory
usage of the job and automatically cleaning up the node in case the jobs fails.