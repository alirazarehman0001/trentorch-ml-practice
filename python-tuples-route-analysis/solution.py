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
    n = len(points)

    if n == 0:
        return ({}, None, 0, 0, 0)

    if n == 1:
        pt = points[0]
        return ({pt: 1}, (pt, pt), 0, 0, 0)

    visit_counts = {}
    min_x, min_y = points[0]
    max_x, max_y = points[0]

    for x, y in points:
        if (x, y) in visit_counts:
            visit_counts[(x, y)] += 1
        else:
            visit_counts[(x, y)] = 1

        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    bounding_box = ((min_x, min_y), (max_x, max_y))

    path_length = 0
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        path_length += abs(x1 - x2) + abs(y1 - y2)

    first, *_, last = points
    net_displacement = abs(first[0] - last[0]) + abs(first[1] - last[1])

    revisit_count = n - len(visit_counts)

    return (
        visit_counts,
        bounding_box,
        path_length,
        net_displacement,
        revisit_count,
    )
