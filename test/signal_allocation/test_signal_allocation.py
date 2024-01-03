"""Test Signal Allocation Implementation."""

import unittest

from signal_allocation.signal_allocation import signal_allocation


class SignalAllocationTest(unittest.TestCase):
    """Class SignalAllocationTest."""

    def setUp(self):
        """setUp."""
        self.sig_allo = signal_allocation.SignalAllocation()

    def test_tower01(self):
        """Test #01 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation(
            random_num_towers=1000,
            random_min_power=0.01,
            random_max_power=0.1,
            max_allowed_radio_signals=None)
        self.assertEqual(True, self.sig_allo.create_mapping())
        self.sig_allo.towers.visualize_towers()
        self.assertEqual(self.sig_allo.is_valid(), True)

    def test_tower02(self):
        """Test #02 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation()
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower03(self):
        """Test #03 for Signal Allocation."""
        test_towers = [('a', (0.5, 0.75), 0.2), ('b', (0.3, 0.75), 0.2),
                       ('c', (0.7, 0.75), 0.2), ('d', (0.5, 0.25), 0.2),
                       ('e', (0.3, 0.25), 0.2), ('f', (0.7, 0.25), 0.2)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower04(self):
        """Test #04 for Signal Allocation."""
        test_towers = [(1, (0.6, 0.67), 0.15), (2, (0.4, 0.67), 0.15),
                       (3, (0.3, 0.5), 0.15), (4, (0.4, 0.33), 0.15),
                       (5, (0.6, 0.33), 0.15), (6, (0.7, 0.5), 0.15)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower05(self):
        """Test #05 for Signal Allocation."""
        test_towers = [(0, (0.80, 0.50), 0.15), (1, (0.69, 0.73), 0.15),
                       (2, (0.43, 0.79), 0.15), (3, (0.23, 0.63), 0.15),
                       (4, (0.23, 0.37), 0.15), (5, (0.43, 0.21), 0.15),
                       (6, (0.69, 0.27), 0.15)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower06(self):
        """Test #06 for Signal Allocation."""
        test_towers = [(0, (0.17, 0.5), 0.43), (1, (0.33, 0.5), 0.27),
                       (2, (0.5, 0.5), 0.2), (3, (0.67, 0.5), 0.27),
                       (4, (0.83, 0.5), 0.43)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower07(self):
        """Test #07 for Signal Allocation."""
        test_towers = [('a', (0.5, 0.75), 0.2), ('b', (0.3, 0.75), 0.2),
                       ('c', (0.7, 0.75), 0.2), ('d', (0.5, 0.25), 0.2),
                       ('e', (0.3, 0.25), 0.2), ('f', (0.7, 0.25), 0.2)]
        self.sig_allo = signal_allocation.SignalAllocation(
            tower_list=test_towers, max_allowed_radio_signals=2)
        self.assertEqual(False, self.sig_allo.create_mapping())
        self.assertEqual(False, self.sig_allo.is_valid())

    def test_tower08(self):
        """Test #08 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation()
        self.assertEqual(self.sig_allo.get_towers(), self.sig_allo.towers)

    def test_tower09(self):
        """Test #09 for Signal Allocation."""
        test_towers = [(0, (0.17, 0.5), 0.43), (1, (0.33, 0.5), 0.27),
                       (2, (0.5, 0.5), 0.2), (3, (0.67, 0.5), 0.27),
                       (4, (0.83, 0.5), 0.43)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.assertEqual(self.sig_allo.is_valid(), False)

    def test_tower10(self):
        """Test #10 for Signal Allocation."""
        test_towers = [(0, (0.80, 0.50), 0.15), (1, (0.69, 0.73), 0.15),
                       (2, (0.43, 0.79), 0.15), (3, (0.23, 0.63), 0.15),
                       (4, (0.23, 0.37), 0.15), (5, (0.43, 0.21), 0.15),
                       (6, (0.69, 0.27), 0.15)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.assertEqual(self.sig_allo.get_num_radio_signals(), 0)
        self.sig_allo.create_mapping()
        self.assertEqual(self.sig_allo.get_num_radio_signals(), 3)

    def test_tower11(self):
        """Test #11 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation(
            random_num_towers=400,
            random_min_power=0.02,
            random_max_power=0.08,
            max_allowed_radio_signals=None)
        self.assertEqual(True, self.sig_allo.create_mapping())
        # self.sig_allo.towers.visualize_towers()
        self.assertEqual(self.sig_allo.is_valid(), True)

    def test_tower12(self):
        """Test #12 for Signal Allocation."""
        test_towers = [(1, (0.2, 0.2), 0.1), (2, (0.4, 0.2), 0.1),
                       (3, (0.6, 0.2), 0.1), (4, (0.2, 0.4), 0.1),
                       (5, (0.4, 0.4), 0.1), (6, (0.6, 0.4), 0.1),
                       (7, (0.2, 0.6), 0.1), (8, (0.4, 0.6), 0.1),
                       (9, (0.6, 0.6), 0.1)]
        self.sig_allo = signal_allocation.SignalAllocation(tower_list=test_towers)
        self.sig_allo.create_mapping()
        self.assertEqual(True, self.sig_allo.is_valid())

    def test_tower13(self):
        """Test #13 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation(
            random_num_towers=400,
            random_min_power=0.02,
            random_max_power=0.08,
            max_allowed_radio_signals=2)
        self.assertEqual(False, self.sig_allo.create_mapping())
        # self.sig_allo.towers.visualize_towers()
        self.assertEqual(self.sig_allo.is_valid(), False)

    def test_tower14(self):
        """Test #14 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation(
            random_num_towers=100,
            random_min_power=0.05,
            random_max_power=0.2,
            max_allowed_radio_signals=None)
        self.assertEqual(True, self.sig_allo.create_mapping())
        self.sig_allo.towers.visualize_towers()
        self.assertEqual(self.sig_allo.is_valid(), True)

    def test_tower15(self):
        """Test #15 for Signal Allocation."""
        self.sig_allo = signal_allocation.SignalAllocation()
        self.assertEqual(True, self.sig_allo.create_mapping())
        # self.sig_allo.towers.visualize_towers()
        self.assertEqual(self.sig_allo.is_valid(), True)
        print(self.sig_allo.get_graph_list_as_ids(self.sig_allo.graph_list))
