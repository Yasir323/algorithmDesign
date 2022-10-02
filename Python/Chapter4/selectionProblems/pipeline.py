"""
Professor Olay is consulting for an oil company, which is planning a large pipeline running east 
to west through an oil field of nn wells. The company wants to connect a spur pipeline from each 
well directly to the main pipeline along a shortest route (either north or south), as shown in 
Figure 9.2. Given the xx- and yy-coordinates of the wells, how should the professor pick the 
optimal location of the main pipeline, which would be the one that minimizes the total length of 
the spurs? Show how to determine the optimal location in linear time.
                                                        x
        x                                               |
        |   x                                           |
        |   |               x                           |
        |   |       x       |                           |
        |   |       |       |           x               |
------------------------------------------------------------------------
    |           |                |                |
    |           |                |                x
    |           x                |
    x                            |
                                 x


If n is odd, we pick the y coordinate of the main pipeline to be equal to the median of all the y 
coordinates of the wells.

If n is even, we pick the y coordinate of the pipeline to be anything between the y coordinates of the 
wells with y-coordinates which have order statistics floor ((n + 1) / 2) and the ceil ((n + 1) / 2). These 
can all be found in linear time using the algorithm from this section.
"""


def optimal_place(coordinates, n):
    """Just median is also fine."""
    y_coords = [x[1] for x in coordinates]
    y_coords.sort()
    if n % 2 != 0:
        return y_coords[n//2]
    return (y_coords[n//2] + y_coords[n//2-1]) / 2


if __name__ == "__main__":
    coords = [(1, 2), (2, 3), (3, -5), (4, -1), (5, 0), (6, 4)]
    coords2 = [(1, 2), (2, 3), (3, -5), (4, -1), (6, 4)]
    print(optimal_place(coords, len(coords)))
    print(optimal_place(coords2, len(coords2)))
