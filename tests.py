import statistics
import random
import os
import sys
import numpy as np
import matplotlib as mpl
import data_viz as dv
import math_lib as ml
import plot_gtex as pg
import unittest
from PIL import Image


class Test_dv(unittest.TestCase):
    """Tests dv.py functionality"""

    def setUp(self):
        already = Image.new('RGB', (1, 1))
        already.save('already.png', "PNG")

    def test_boxplot_already_exists(self):
        with self.assertRaises(OSError):
            dv.boxplot([1, 2, 3, 4], 'already.png', 'SMTS', 'gene', 'groupco\
            lname')

    def test_hist_already_exists(self):
        with self.assertRaises(OSError):
            dv.histogram([1, 2, 3, 4], 'already.png')

    def test_combo_already_exists(self):
        with self.assertRaises(OSError):
            dv.combo([1, 2, 3, 4], 'already.png')

    def test_box_none_list(self):
        with self.assertRaises(ValueError):
            dv.boxplot(None, 'novel.png', 'SMTS', 'gene', 'groupcolname')

    def test_box_empty_list(self):
        with self.assertRaises(ValueError):
            dv.boxplot([], 'novel2.png', 'SMTS', 'gene', 'groupcolname')

    def test_box_1d(self):
        with self.assertRaises(TypeError):
            dv.boxplot([1, 2, 3], 'novel3.png', 'SMTS', 'gene', 'groupcolname')


class Test_ml(unittest.TestCase):
    """A set of unit tests for ml"""

    def setUp(self):
        self.direct_compute_array = []
        for i in range(100):
            rand_int = random.randint(1, 100)
            self.direct_compute_array.append(rand_int)

        self.direct_mean_val = statistics.mean(self.direct_compute_array)
        self.direct_std_val = statistics.pstdev(self.direct_compute_array)

    # Tests for list_mean method
    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            ml.list_mean([])

    def test_mean_none(self):
        with self.assertRaises(ValueError):
            ml.list_mean(None)

    def test_mean_only_str(self):
        with self.assertRaises(ValueError):
            ml.list_mean(['a', 'b', 'c'])

    def test_mean_mixed_list(self):
        self.assertEqual(ml.list_mean(['a', 2, 'c', '4']), 3)

    def test_mean_rand_ints(self):
        self.assertEqual(ml.list_mean(self.direct_list_mean_array),
                         self.direct_mean_val)

    # Tests for list_stdev method
    def test_stdev_none(self):
        with self.assertRaises(ValueError):
            ml.list_stdev(None)

    def test_stdev_empty(self):
        with self.assertRaises(ValueError):
            ml.list_stdev([])

    def test_stdev_one_el(self):
        with self.assertRaises(ValueError):
            ml.list_stdev([88])

    def test_stdev_only_str(self):
        with self.assertRaises(ValueError):
            ml.list_stdev(['a', 'b', 'c'])

    def test_stdev_mixed_list(self):
        self.assertEqual(ml.list_stdev(['a', 2, 'c', '4', 'd']), 1)

    def test_mean_rand_ints(self):
        self.assertAlmostEqual(ml.list_stdev(self.direct_compute_array),
                               self.direct_std_val)


if __name__ == '__main__':
    unittest.main()
