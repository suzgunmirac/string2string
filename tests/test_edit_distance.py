"""
    Unit test cases for edit_distance.py
"""
import unittest
from unittest import TestCase

from string2string.edit_distance import EditDistAlgs


class EditDistanceTestCase(TestCase):
    def test_levenshtein_edit_distance_unit_operations(self):
        ## Case 1: Costs of insertion, deletion, and substitution are all 1.
        algs_unit = EditDistAlgs()
        # Example 1
        dist = algs_unit.levenshtein_edit_distance('aa', 'bb')
        self.assertEqual(dist, 2.)
        # Example 2
        dist = algs_unit.levenshtein_edit_distance('monty-python', 'monty-python')
        print(dist)
        self.assertEqual(dist, 0.)
        # Example 3
        dist = algs_unit.levenshtein_edit_distance('kitten', 'sitting')
        self.assertEqual(dist, 3.)
        # Example 4
        dist = algs_unit.levenshtein_edit_distance('sitting', 'kitten')
        self.assertEqual(dist, 3.)
        # Example 5
        dist = algs_unit.levenshtein_edit_distance('aaaaa', 'a')
        self.assertEqual(dist, 4.)
        # Example 6
        dist = algs_unit.levenshtein_edit_distance('', 'abcdef')
        self.assertEqual(dist, 6.)
        # Example 7
        dist = algs_unit.levenshtein_edit_distance('abcdef', '')
        self.assertEqual(dist, 6.)
        # Example 8
        dist = algs_unit.levenshtein_edit_distance('algorithm', 'al-Khwarizmi')
        self.assertEqual(dist, 8.)
        # Example 9
        dist = algs_unit.levenshtein_edit_distance('qrrq', 'rqqr')
        self.assertEqual(dist, 3.)

    def test_levenshtein_edit_distance_weighted_operations(self):
        ## Case 2: insertion = 2., deletion = 2., substitution = 1., match = 0.
        algs_weighted = EditDistAlgs(
            insert_weight=2.,
            delete_weight=2.,
            match_weight=0., 
            substite_weight=1.
        )
        # Example 1
        dist = algs_weighted.levenshtein_edit_distance('aa', 'bb')
        self.assertEqual(dist, 2.)
        # Example 2
        dist = algs_weighted.levenshtein_edit_distance('aca', 'bcb')
        self.assertEqual(dist, 2.)
        # Example 3
        dist = algs_weighted.levenshtein_edit_distance('aa', '')
        self.assertEqual(dist, 4.)
        # Example 4
        dist = algs_weighted.levenshtein_edit_distance('', 'aa')
        self.assertEqual(dist, 4.)
        # Example 5
        dist = algs_weighted.levenshtein_edit_distance('witty', 'witty')
        self.assertEqual(dist, 0.)
        # Example 6
        dist = algs_weighted.levenshtein_edit_distance('ttss', 'stst')
        self.assertEqual(dist, 2.)
        

if __name__ == '__main__':
    unittest.main()