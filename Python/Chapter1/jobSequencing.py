# JOB SEQUENCING PROBLEM USING GREEDY ALGORITHM
"""
Given an array of jobs where every job has a deadline and associated priority if the job 
is finished before the deadline. It is also given that every job takes a single unit of 
time, so the minimum possible deadline for any job is 1. How to maximize total priority 
if only one job can be scheduled at a time.
"""


def printJobScheduling(arr):
    # Sort by priority
    arr.sort(key=lambda x: x[2], reverse=True)
    i = 0
    jobs = []
    while i < len(arr):
        if i == 1:
            jobs.append(arr[i][0])
        else:
            if arr[i][1] <= arr[i-1][1]:
                i += 1
                continue
            else:
                jobs.append(arr[i][0])
        i += 1
    print(' '.join(jobs))


# Driver COde
def main():
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
    
    print("Following is maximum priority sequence of jobs") 
    # Function Call
    printJobScheduling(arr)


if __name__ == '__main__':
    main()
