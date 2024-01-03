"""Signal Allocation."""

import sys
from signal_allocation.towers import towers


# pylint: disable=R0913

class SignalAllocation:
    """Signal Allocation Class."""

    def __init__(self, tower_list=None, max_allowed_radio_signals=None,
                 random_num_towers=10, random_min_power=0.1, random_max_power=0.2):
        """Init the Signal Allocation Class."""
        self.towers = towers.Towers(
            tower_list,
            random_num_towers,
            random_min_power,
            random_max_power)

        if max_allowed_radio_signals is None:
            self.max_signals = random_num_towers
        else:
            self.max_signals = max_allowed_radio_signals

        # Used to store the graph list
        self.graph_list = []
        if len(self.towers.towers) > 970:
            sys.setrecursionlimit(len(self.towers.towers) + 30)

    def get_towers_as_graph(self):
        """Return a list of graphs that represents the tower layout."""
        # Create a visited list to keep track of visited towers
        visited = []

        # tower_indexate through towers and perform a BFS until all have been visited
        for tower in self.towers.get_towers():

            # Only want to perform another BFS if tower is apart of a new string of towers
            if tower not in visited:
                graph = {}
                visited.append(tower)
                queue = [tower]
                graph[tower] = []

                # Main BFS loop that explores overlapping towers
                while queue:
                    node = queue.pop(0)

                    # Check adjacent/overlapping towers
                    for overlapping_tower in self.towers.get_overlapping_towers(node):
                        if overlapping_tower not in visited:

                            # Visit tower and add to queue (for BFS)
                            visited.append(overlapping_tower)
                            queue.append(overlapping_tower)

                            # Add tower to undirected graph
                            graph[node].append(overlapping_tower)
                            graph[overlapping_tower] = [node]

                        # Ensure that already visited towers are accounted for
                        elif overlapping_tower not in graph[node]:
                            graph[node].append(overlapping_tower)

                # Add completed graph to the list
                self.graph_list.append(graph)

    def is_valid_signal(self, graph_index, tower, signal):
        """Check if the signal is valid."""
        for overlapping_tower in self.graph_list[graph_index][tower]:
            if overlapping_tower.signal == signal:
                return False
        return True

    def create_mapping_helper(self, graph_index, tower, tower_index):
        """Help create mapping."""
        # Base Case: We reached end of dictionary
        if tower_index == len(list(self.graph_list[graph_index])) - 1:
            # Make sure that last element gets assigned a color
            for signal in range(1, self.max_signals + 1):
                if self.is_valid_signal(graph_index, tower, signal):
                    tower.signal = signal
                    return True
            return False

        for signal in range(1, self.max_signals + 1):
            if self.is_valid_signal(graph_index, tower, signal):
                tower.signal = signal
                if self.create_mapping_helper(
                        graph_index, list(self.graph_list[graph_index])[tower_index + 1],
                        tower_index + 1) is True:
                    return True
                tower.signal = 0

        return False

    def create_mapping(self):
        """Map each tower to a signal such that overlapping towers do not share the same signal."""
        # Get the tower layout as a list of graphs
        self.get_towers_as_graph()

        for graph_index, _ in enumerate(self.graph_list):
            # Perform the graph coloring algorithm here
            if not self.create_mapping_helper(
                    graph_index, list(self.graph_list[graph_index])[0], 0):
                return False

        return True

    def get_towers(self):
        """Return the Towers object."""
        return self.towers

    def get_num_radio_signals(self):
        """Return the number of signals used in the mapping."""
        number_signals = 0
        for tower in self.towers.towers:
            if tower.signal > number_signals:
                number_signals = tower.signal
        return number_signals

    def is_valid(self):
        """Return true if create mapping was able to be solved, otherwise return false."""
        for tower1, tower2 in self.towers.get_overlaps():
            if tower1.signal == tower2.signal:
                return False
        return True

    def get_graph_list_as_ids(self, graph_list):
        """Return the graph_list as ids."""
        graph_list_id = []

        for graph in graph_list:
            graph_id = {}
            for tower in graph.keys():
                graph_id[tower.tower_id] = []
                for tower2 in graph[tower]:
                    graph_id[tower.tower_id].append(tower2.tower_id)
            graph_list_id.append(graph_id)

        return graph_list_id
