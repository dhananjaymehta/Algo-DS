import math


class Data(object):
    def __init__(self, name):
        self.__name = name
        self.__links = set()

    @property
    def name(self):
        return self.__name

    @property
    def links(self):
        return set(self.__links)

    def add_link(self, other):
        self.__links.add(other)
        other.__links.add(self)

        # The function to look for connected components.


def connected_components(nodes):
    result = []
    nodes = set(nodes)
    while nodes:

        # Get a random node and remove it from the global set.
        n = nodes.pop()

        # This set will contain the next group of nodes connected to each other.
        group = {n}

        # Build a queue with this node in it.
        queue = [n]

        # Iterate the queue.
        # When it's empty, we finished visiting a group of connected nodes.
        while queue:
            # Consume the next item from the queue.
            n = queue.pop(0)

            # Fetch the neighbors.
            neighbors = n.links

            # Remove the neighbors we already visited.
            neighbors.difference_update(group)

            # Remove the remaining nodes from the global set.
            nodes.difference_update(neighbors)

            # Add them to the group of connected nodes.
            group.update(neighbors)

            # Add them to the queue, so we visit them in the next iterations.
            queue.extend(neighbors)

        # Add the group to the list of groups.
        result.append(group)

    # Return the list of groups.
    return result

    # The test code...


def minimalCost(n, pairs):
    nodes_map = {x: Data(x) for x in xrange(1, n + 1)}

    for pair in pairs:
        p, q = int(pair.split(' ')[0]), int(pair.split(' ')[1])
        nodes_map[p].add_link(nodes_map[q])

    # Find all the connected components.
    cost = 0
    for components in connected_components(nodes_map.values()):
        # names = sorted(node.name for node in components)
        # print names
        cost += math.ceil(math.sqrt(len(components)))
    return long(cost)