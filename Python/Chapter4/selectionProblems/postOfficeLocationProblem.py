"""
The post-office location problem is defined as follows. We are given nn points p1, p2,..., pn with 
associated weights w1, w2,..., wn. We wish to find a point p (not necessarily one of the input 
points) that minimizes the sum \sum_{i = 1}^n wi d(p, pi), where d(a, b) is the distance between 
points a and b.
"""

def median(arr, n):
    arr.sort()
    if n % 2 != 0:
        return arr[n//2]
    return (arr[n//2] + arr[n//2-1]) / 2


if __name__ == "__main__":
    points = [
        (5, 2),
        (0, 0),
        (-1, 2),
        (1, -2),
        (3, 3),
    ]
    n = len(points)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    px = median(xs, n)
    py = median(ys, n)
    print(f"Optimal Position: ({px}, {py})")
