# USING GREEDY ALGORITHM
"""
You are given n activities with their start and finish times. 
Select the maximum number of activities that can be performed by a 
single person, assuming that a person can only work on a single 
activity at a time.
"""


def maxActivities(times):
    """Sort the activities based on the finish times first."""
    times = sorted(times, key=lambda x: x[1])
    count = 0
    prev_finish_time = 0
    for start_time, finish_time in times:
        if start_time >= prev_finish_time:
            count += 1
            prev_finish_time = finish_time
    return count


# Driver program to test above function
array = [(3, 4), (0, 6), (1, 2), (8, 9), (5, 9), (5, 7)]
print(maxActivities(array))