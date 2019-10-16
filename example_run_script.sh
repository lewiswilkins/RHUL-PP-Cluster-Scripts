#!bin/bash

# Line below will set the maximum time for the job to run
#PBS -l walltime=10:00:00

JOBDIR=/data/$USER/job_$PBS_JOBID # Sets the name of the job directory
trap "rm -r $JOBDIR; exit" SIGTERM SIGNT SIGHUP TERM KILL # Clears up in the case of job failure
mkdir JOBDIR $&& cd $JOBDIR # Make and enter job directory


source setup_your_environment.sh # Here you would setup your environment 
./your_code_to_run & # Run your code - in background to track memory usage

# The following code will track the peak memory usage
peakvmem = "0 kB"

pid=$!
temppeakvmem="$(cat /proc/${pid}/status | awk '/VmPeak/{print $2" "$3}')"
while [ -e /proc/$pid ]; do
  peakvmem="$temppeakvmem"
  temppeakvmem="$(cat /proc/${pid}/status | awk '/VmPeak/{print $2" "$3}')"
  sleep 10
done
echo "Peak memory usage: "$peakvmem

mv output_file /path/to/wherever # Move off your output file
rm -rf $JOBDIR # Clean up the node
