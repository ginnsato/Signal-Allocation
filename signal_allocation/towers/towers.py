"""Towers."""

import random
import math
from matplotlib.colors import colorConverter
from matplotlib import cm
from matplotlib import text
import matplotlib.pyplot as plt
import numpy as np


class Tower:
    """Tower Class."""

    def __init__(self, tower_id, position, power, signal):
        """Init the Tower Class."""
        # Unique identifier for tower
        self.tower_id = tower_id

        # (x, y): floats between 0 and 1
        self.position = position

        # Power represents how far the tower's signal carries
        self.power = power

        # Signal is positive integer
        self.signal = signal

    def get_power(self):
        """Return the power."""
        return self.power

    def get_position(self):
        """Return the position."""
        return self.position


class Towers:
    """Towers Class."""

    def __init__(self, tower_list=None, random_num_towers=10,
                 random_min_power=0.1, random_max_power=0.2):
        """Init Towers Class."""
        self.towers = []
        if tower_list is not None:
            for tower_id, pos, power in tower_list:
                self.towers.append(Tower(tower_id, pos, power, 0))
        else:
            for tower_id in range(random_num_towers):
                pos = (random.uniform(0, 1), random.uniform(0, 1))
                power = random.uniform(random_min_power, random_max_power)
                self.towers.append(Tower(tower_id, pos, power, 0))

    def add_tower(self, tower_id, position, power, signal=0):
        """Add a new tower to towers."""
        for tow in self.towers:
            tower = tow.tower_id
            if tower == tower_id:
                tow.position = position
                tow.power = power
                tow.signal = signal
                return
        self.towers.append(Tower(tower_id, position, power, signal))

    def remove_tower(self, tower_id):
        """Remove the tower with tower_id."""
        for tow in self.towers:
            tower = tow.tower_id
            if tower == tower_id:
                self.towers.remove(tow)

    def get_overlaps(self):
        """Return a list of tuples of overlapping towers."""
        overlaps = []
        for tower in self.towers:
            overlapping_towers = self.get_overlapping_towers(tower)
            for tower2 in overlapping_towers:
                overlaps.append((tower, tower2))
        return overlaps

    def get_overlapping_towers(self, tower):
        """Return a list of Tower objects that overlap with tower."""
        overlapping_towers = []
        found = False
        for tow in self.towers:
            if tow == tower:
                found = True
                (x_one, y_one) = tow.get_position()
                power1 = tow.get_power()
                break
        if not found:
            return overlapping_towers

        for tow in self.towers:
            if tow != tower:
                (x_two, y_two) = tow.position
                power2 = tow.power
                val = math.sqrt((x_one - x_two)**2 + (y_one - y_two)**2)
                # Check if they overlap
                if val <= power1 + power2:
                    overlapping_towers.append(tow)

        return overlapping_towers

    def get_towers(self):
        """Return a list of all Tower objects."""
        return self.towers

    def get_num_objects(self):
        """Return the number of Tower objects."""
        return len(self.towers)

    def visualize_towers(self):
        """Visualize the tower layout."""
        fig = plt.figure()
        fig.set_size_inches((8, 8))
        axes = plt.Axes(fig, [0., 0., 1., 1.])
        axes.set_axis_off()
        fig.add_axes(axes)
        axes.invert_yaxis()

        towers = self.get_towers()

        if len(towers) > 0:

            max_signal = max(towers, key=lambda x: x.signal).signal
            colors = cm.gist_rainbow(np.linspace(0, 1, max_signal + 1))

            for tow in towers:
                fc_temp = colorConverter.to_rgba(colors[tow.signal], alpha=0.3)
                c_temp = plt.Circle(tow.position, tow.power, fc=fc_temp, label=tow.tower_id)
                axes.add_artist(c_temp)

                """
                txt = text.Text(
                    x=tow.position[0],
                    y=tow.position[1],
                    text="Tower: " + str(
                        tow.tower_id) + "\n" + "Signal: " + str(tow.signal),
                    ha='center',
                    va='center',
                    axes=axes)
                """
                # axes.add_artist(txt)

        fig.savefig('test/test.png')
        plt.show()
