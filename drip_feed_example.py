import time

from queue_management import count_queue_numbers, get_queue

if __name__ == "__main__":
    """In this example, we assume you have 10000 jobs to run.
    This is far too many for the farm to handle at once and
    requires you to 'drip feed' the jobs(do the schedulers job
    for it..) into the queue. What we will do is have the script
    check the number of jobs in queue every 20s and only submit
    a job when the total number running in the long queue is
    below 1950 and the total number of jobs is below 3900."""

    n_jobs = 10000  # You have 10000 jobs to submit
    x = 0
    while x < n_jobs:
        # Want to get the number of jobs in the long queue
        long_queue = get_queue(queue_name="long")
        n_long_queue = count_queue_numbers(queue=long_queue, sum_output=True)

        # Now the number of jobs in all queues
        full_queue = get_queue()
        n_full_queue = count_queue_numbers(queue=full_queue, sum_output=True)

        if n_long_queue < 1950 and n_full_queue < 3900:
            print("Submitting job!")
            # Here you would insert your code to submit your job.
            x += 1
        else:
            print(
                """{0} jobs in long queue and {1} in total queue. Waiting 20s to
                retry""".format(n_long_queue, n_full_queue))
            time.sleep(20)
