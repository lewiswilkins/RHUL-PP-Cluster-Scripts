import subprocess


def count_queue_numbers(queue, sum_output=False):
    """Counts the number of jobs running and queued from a given queue.
        Args:
            queue - list of jobs in the queue returned from get_queue
            sum_output - return the sum of the running and queued
        Returns:
            n_run - number of jobs running
            n_queue - number of jobs queued
        or
            n_summed - sum of n_run and n_queue"""

    n_run = 0
    n_queue = 0
    for line in o.split("\n"):
        if "R " in line:
            n_run += 1
        if "Q " in line:
            n_queue += 1
    if sum_output:
        return n_run + n_queue
    else:
        return n_queue, n_run


def get_queue(queue_name=""):
    """Calls qstat to get queue information.
        Args:
            queue_name - the queue or username to filter on. For username,
            prefix with -u. e.g. -u username
       Returns:
            list of jobs in the queue. """
    print(get_qstat_arg(queue_name))
    q = subprocess.Popen(
        _get_qstat_arg(queue_name), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, stdin=subprocess.PIPE
        )
    o, e = q.communicate()

    return o


def _get_qstat_arg(string):
    string = "qstat " + string
    return string.split(" ")
