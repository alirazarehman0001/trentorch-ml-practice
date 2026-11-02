def analyze_route(points: list) -> tuple:
    """
    `points` is a list of (x, y) tuples of ints, in the order
    the route visits them. Return a 5-element tuple:

      (visit_counts, bounding_box, path_length,
       net_displacement, revisit_count)

    where:
      - visit_counts: a dictionary mapping each distinct
        (x, y) tuple to how many times it appears in `points`.
      - bounding_box: a tuple ((min_x, min_y), (max_x, max_y))
        covering all points. Compute it with a loop and
        comparisons (do not use min() or max()).
      - path_length: the sum of the Manhattan distances between
        each consecutive pair of points. Use an index loop.
      - net_displacement: the Manhattan distance between the
        first and last point. Obtain the first and last points
        with extended unpacking: first, *_, last = points
        (handle a single-point route separately).
      - revisit_count: len(points) minus the number of distinct
        points, i.e. how many visits were to a point already
        seen.

    An empty `points` returns ({}, None, 0, 0, 0).
    A single point returns:
      ({point: 1}, (point, point), 0, 0, 0)

    `points` and its tuples must not be modified.
    """
    if len(points) == 0:
        return ({}, None, 0, 0, 0)

    visit_count = {}
    for point in points:
        if point in visit_count:
            visit_count[point] += 1
        else: 
            visit_count[point] = 1

    min_x = min_y = max_x = max_y = None
    for x, y in points:
        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_x is None or x > max_x:
            max_x = x
        if max_y is None or y > max_y:
            max_y = y
    bounding_box = ((min_x, min_y), (max_x, max_y))

    path_length = 0
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        path_length += abs(x2 - x1) + abs(y2 - y1)

    if len(points) == 1:
        net_displacement = 0
    else:
        first, *_, last = points
        x1, y1 = first
        x2, y2 = last
        net_displacement = abs(x2 - x1) + abs(y2 - y1)

    revist_count = len(points) - len(visit_count)

    return (visit_count, bounding_box, path_length, net_displacement, revist_count)
