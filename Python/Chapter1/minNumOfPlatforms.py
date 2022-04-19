# MINIMUM NUMBER OF PLATFORMS REQUIRED USING GREEDY ALGO
"""
Given the arrival and departure times of all trains 
that reach a railway station, the task is to find the 
minimum number of platforms required for the railway 
station so that no train waits. 

We are given two arrays that represent the arrival and 
departure times of trains that stop.
"""


def find_platform(arrivals, departures, n):
    # Assuming the arrays are sorted by departure times
    num_platforms = 1
    max_platforms = num_platforms
    max_dep = departures[0]
    for i in range(1, n):
        if arrivals[i] <= max_dep:
            num_platforms += 1
            if max_platforms < num_platforms:
                max_platforms = num_platforms
        else:
            num_platforms = 1
        if departures[i] > max_dep:
            max_dep = departures[i]
    return max_platforms
    

def main():
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(arr)
    print(find_platform(arr, dep, n))


if __name__ == '__main__':
    main()