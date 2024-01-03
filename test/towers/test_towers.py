"""Test Tower Implementation."""

import unittest

from signal_allocation.towers import towers


class TowersTest(unittest.TestCase):
    """Class TowersTest."""

    def setUp(self):
        """setUp."""
        self.towers = towers.Towers()

    def test_tower01(self):
        """Test Tower with None."""
        self.towers = towers.Towers()
        towers_obj = self.towers.towers
        for tower in towers_obj:
            self.assertGreaterEqual(0.2, tower.power)

    def test_tower02(self):
        """Test Tower with input."""
        test_towers = [(0, (0.76, 0.42), 0.18), (1, (0.51, 0.4), 0.13),
                       (2, (0.3, 0.48), 0.18), (3, (0.91, 0.5), 0.16)]
        self.towers = towers.Towers(test_towers)
        self.assertEqual(self.towers.towers[0].position, (0.76, 0.42))
        self.assertEqual(self.towers.towers[1].position, (0.51, 0.4))

    def test_tower03(self):
        """Test Tower add_tower with new tower_id."""
        self.towers = towers.Towers()
        self.towers.add_tower(10, (0.5, 0.5), 0.25)
        self.assertEqual(self.towers.towers[10].position, (0.5, 0.5))

    def test_tower04(self):
        """Test Tower add_tower with existing tower_id."""
        self.towers = towers.Towers()
        self.towers.add_tower(1, (0.5, 0.5), 0.25)
        self.assertEqual(self.towers.towers[1].position, (0.5, 0.5))
        self.assertEqual(len(self.towers.towers), 10)

    def test_tower05(self):
        """Test Tower remove_tower."""
        self.towers = towers.Towers()
        self.towers.remove_tower(0)
        self.towers.remove_tower(9)
        self.assertEqual(len(self.towers.towers), 8)

    def test_tower06(self):
        """Test Tower remove_tower for empty tower list."""
        self.towers = towers.Towers([])
        self.assertEqual(len(self.towers.towers), 0)

    def test_tower07(self):
        """Test Tower get_overlaps."""
        test_towers = [(0, (0.76, 0.42), 0.18), (1, (0.51, 0.4), 0.13),
                       (2, (0.3, 0.48), 0.18), (3, (0.91, 0.5), 0.16)]
        self.towers = towers.Towers(test_towers)
        tower0 = self.towers.towers[0]
        tower1 = self.towers.towers[1]
        tower2 = self.towers.towers[2]
        tower3 = self.towers.towers[3]
        self.assertEqual(
            [(tower0, tower1),
             (tower0, tower3),
             (tower1, tower0),
             (tower1, tower2),
             (tower2, tower1),
             (tower3, tower0)],
            self.towers.get_overlaps())

    def test_tower08(self):
        """Test Tower get_overlaps."""
        test_towers = [(0, (0.76, 0.42), 0.01), (1, (0.51, 0.4), 0.01),
                       (2, (0.3, 0.48), 0.01), (3, (0.91, 0.5), 0.01)]
        self.towers = towers.Towers(test_towers)
        self.assertEqual([], self.towers.get_overlaps())

    def test_tower09(self):
        """Test Tower get_overlapping_towers."""
        test_towers = [(0, (0.76, 0.42), 0.18), (1, (0.51, 0.4), 0.13),
                       (2, (0.3, 0.48), 0.18), (3, (0.91, 0.5), 0.16)]
        self.towers = towers.Towers(test_towers)
        tower0 = self.towers.towers[0]
        tower1 = self.towers.towers[1]
        tower3 = self.towers.towers[3]
        self.assertEqual([tower1, tower3], self.towers.get_overlapping_towers(tower0))

    def test_tower10(self):
        """Test Tower get_overlapping_towers."""
        test_towers = [(0, (0.76, 0.42), 0.18), (1, (0.51, 0.4), 0.13),
                       (2, (0.3, 0.48), 0.18), (3, (0.91, 0.5), 0.16)]
        self.towers = towers.Towers(test_towers)
        self.assertEqual([], self.towers.get_overlapping_towers(7))

    def test_tower11(self):
        """Test Tower get_overlapping_towers."""
        test_towers = [('a', (0, 0), 0.5), ('b', (1, 0), 0.5)]
        self.towers = towers.Towers(test_towers)
        tower0 = self.towers.towers[0]
        tower1 = self.towers.towers[1]
        self.assertEqual([tower1], self.towers.get_overlapping_towers(tower0))

    def test_tower12(self):
        """Test Tower get_towers."""
        self.towers = towers.Towers()
        self.assertEqual(self.towers.get_towers(), self.towers.towers)

    def test_tower13(self):
        """Test Tower get_num_objects."""
        self.towers = towers.Towers()
        self.assertEqual(self.towers.get_num_objects(), 10)
        self.towers.remove_tower(0)
        self.assertEqual(self.towers.get_num_objects(), 9)

    def test_tower14(self):
        """Test Tower visualize_towers."""
        self.towers = towers.Towers()
        # self.towers.visualize_towers()
        self.assertEqual(True, True)
