"""Search helpers. Complete the five function bodies, then run the doctests."""


def number_lines(lines):
    """Return (line_number, text) tuples, counting from 1.

    >>> number_lines(['Library hours', '', 'Open late'])
    [(1, 'Library hours'), (2, ''), (3, 'Open late')]
    >>> number_lines([])
    []
    """

    return[line for line in enumerate(lines,1)]


def matching_lines(lines, query):
    """Return numbered lines containing query, ignoring case.

    An empty query returns no matches. Preserve the original text and numbers.

    >>> matching_lines(['Library hours', '', 'LIBRARY cafe'], 'library')
    [(1, 'Library hours'), (3, 'LIBRARY cafe')]
    >>> matching_lines(['Library hours'], '')
    []
    >>> matching_lines(['Library hours'], 'pool')
    []
    """
    return[line for line in enumerate(lines,1) 
           if (query.lower() in line[1].lower()) 
           and not query.lower()=='']


def group_matches(documents, query):
    """Return one list of matching lines per document, including empty lists.

    >>> group_matches([['Library map'], ['Pool hours'], ['LIBRARY cafe']], 'library')
    [[(1, 'Library map')], [], [(1, 'LIBRARY cafe')]]
    >>> group_matches([], 'library')
    []
    """
    return [[line for line in (enumerate(document,1)) 
            if query.lower() in line[1].lower()] 
            for document in documents]

def flatten_matches(names, groups):
    """Return (filename, line_number, text) tuples in file and line order.

    names and groups have equal lengths. Filenames are unique.

    >>> flatten_matches(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    [('a.txt', 2, 'Map')]
    >>> flatten_matches([], [])
    []
    """

    return [((x,) + y) for x, y in zip(names, (item for group in groups for item in group))]


def match_counts(names, groups):
    """Return a dictionary of filename: number of matching lines, including zeros.

    names and groups have equal lengths. Filenames are unique.

    >>> match_counts(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    {'a.txt': 1, 'b.txt': 0}
    >>> match_counts([], [])
    {}
    """
    return {x : len(y) for x, y in zip(names, (group for group in groups))}
