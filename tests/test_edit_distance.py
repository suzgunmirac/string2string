"""
    Unit test cases for edit_distance.py
"""
from dis import dis
import unittest
from unittest import TestCase

from string2string.edit_distance import EditDistAlgs


class EditDistanceTestCase(TestCase):
    def test_levenshtein_edit_distance_unit_operations(self):
        ## Case 1: Costs of insertion, deletion, and substitution are all 1.
        algs_unit = EditDistAlgs()
        # Example 0
        dist = algs_unit.levenshtein_edit_distance("", "")
        self.assertEqual(dist, 0.0)
        # Example 1
        dist = algs_unit.levenshtein_edit_distance("aa", "bb")
        self.assertEqual(dist, 2.0)
        # Example 2
        dist = algs_unit.levenshtein_edit_distance("monty-python", "monty-python")
        print(dist)
        self.assertEqual(dist, 0.0)
        # Example 3
        dist = algs_unit.levenshtein_edit_distance("kitten", "sitting")
        self.assertEqual(dist, 3.0)
        # Example 4
        dist = algs_unit.levenshtein_edit_distance("sitting", "kitten")
        self.assertEqual(dist, 3.0)
        # Example 5
        dist = algs_unit.levenshtein_edit_distance("aaaaa", "a")
        self.assertEqual(dist, 4.0)
        # Example 6
        dist = algs_unit.levenshtein_edit_distance("", "abcdef")
        self.assertEqual(dist, 6.0)
        # Example 7
        dist = algs_unit.levenshtein_edit_distance("abcdef", "")
        self.assertEqual(dist, 6.0)
        # Example 8
        dist = algs_unit.levenshtein_edit_distance("algorithm", "al-Khwarizmi")
        self.assertEqual(dist, 8.0)
        # Example 9
        dist = algs_unit.levenshtein_edit_distance("qrrq", "rqqr")
        self.assertEqual(dist, 3.0)
        # Example 10
        dist = algs_unit.levenshtein_edit_distance(["kurt", "godel"], ["godel", "kurt"])
        self.assertEqual(dist, 2.0)
        # Example 11
        dist = algs_unit.levenshtein_edit_distance(
            ["kurt", "godel", "kurt"], ["godel", "kurt"]
        )
        self.assertEqual(dist, 1.0)

    def test_levenshtein_edit_distance_weighted_operations(self):
        ## Case 2: insertion = 2., deletion = 2., substitution = 1., match = 0.
        algs_weighted = EditDistAlgs(
            insert_weight=2.0, delete_weight=2.0, match_weight=0.0, substite_weight=1.0
        )
        # Example 1
        dist = algs_weighted.levenshtein_edit_distance("aa", "bb")
        self.assertEqual(dist, 2.0)
        # Example 2
        dist = algs_weighted.levenshtein_edit_distance("aca", "bcb")
        self.assertEqual(dist, 2.0)
        # Example 3
        dist = algs_weighted.levenshtein_edit_distance("aa", "")
        self.assertEqual(dist, 4.0)
        # Example 4
        dist = algs_weighted.levenshtein_edit_distance("", "aa")
        self.assertEqual(dist, 4.0)
        # Example 5
        dist = algs_weighted.levenshtein_edit_distance("witty", "witty")
        self.assertEqual(dist, 0.0)
        # Example 6
        dist = algs_weighted.levenshtein_edit_distance("ttss", "stst")
        self.assertEqual(dist, 2.0)

    def test_hamming_edit_distance(self):
        algs_unit = EditDistAlgs()
        # Example 1
        dist = algs_unit.hamming_distance("aa", "bb")
        self.assertEqual(dist, 2.0)
        # Example 2
        dist = algs_unit.hamming_distance("aac", "abc")
        self.assertEqual(dist, 1.0)
        # Example 3
        dist = algs_unit.hamming_distance("Turing1912", "during1921")
        self.assertEqual(dist, 3.0)
        # Example 4
        dist = algs_unit.hamming_distance("John von Neumann", "John von Neumann")
        self.assertEqual(dist, 0.0)
        # Example 5
        dist = algs_unit.hamming_distance("Earth", "earth")
        self.assertEqual(dist, 1.0)
        # Example 6
        with self.assertRaises(ValueError):
            dist = algs_unit.hamming_distance(" ", "abc")
        # Example 7
        dist = algs_unit.hamming_distance("", "")
        self.assertEqual(dist, 0.0)
        # Example 8
        dist = algs_unit.hamming_distance(
            ["", "abc", "234", "#"], ["", "abc", "123", "#"]
        )
        self.assertEqual(dist, 1.0)
        # Example 9
        dist = algs_unit.hamming_distance(
            ["a", "ab", "abc", "abcd", "abc", "ab", "a"],
            ["a", "ab", "abc", "abcd", "abc", "ab", "a"],
        )
        self.assertEqual(dist, 0.0)

    def test_longest_common_subsequence(self):
        algs_unit = EditDistAlgs()
        # Example 1
        dist, candidates = algs_unit.longest_common_subsequence(
            "aa", "aa", printBacktrack=True
        )
        self.assertEqual(dist, 2.0)
        self. assertCountEqual(candidates, ["aa"])
        # Example 2
        dist, candidates = algs_unit.longest_common_subsequence(
            "ab", "ba", printBacktrack=True
        )
        self.assertEqual(dist, 1.0)
        self. assertCountEqual(candidates, ["a", "b"])
        # Example 3
        dist, candidates = algs_unit.longest_common_subsequence(
            "ab", "cd", printBacktrack=True
        )
        self.assertEqual(dist, 0.0)
        self. assertCountEqual(candidates, [""])
        # Example 4
        dist, candidates = algs_unit.longest_common_subsequence(
            "ab", "xxaaabyy", printBacktrack=True
        )
        self.assertEqual(dist, 2.0)
        self. assertCountEqual(candidates, ["ab"])
        # Example 5
        dist, candidates = algs_unit.longest_common_subsequence(
            "abcd", "xcxaaabydy", printBacktrack=True
        )
        self.assertEqual(dist, 3.0)
        self. assertCountEqual(candidates, ["abd"])
        # Example 6
        dist, candidates = algs_unit.longest_common_subsequence(
            "aabbccdd", "dcdcbaba", printBacktrack=True
        )
        self.assertEqual(dist, 2.0)
        self. assertCountEqual(candidates, ["dd", "cc", "bb", "aa", "cd", "ab"])

        # Example 7
        dist, candidates = algs_unit.longest_common_subsequence(
            ["abcd"], ["xcxaaabydy"], printBacktrack=True, boolListOfList=True
        )
        self.assertEqual(dist, 0.0)
        self. assertCountEqual(candidates, [])
        # Example 8
        dist, candidates = algs_unit.longest_common_subsequence(
            ["a", "bb", "c"],
            ["a", "bb", "c"],
            printBacktrack=True,
            boolListOfList=True,
        )
        self.assertEqual(dist, 3.0)
        self. assertCountEqual(candidates, [["a", "bb", "c"]])
        # Example 9
        dist, candidates = algs_unit.longest_common_subsequence(
            ["a", "b", "c", "dd"],
            ["x", "c", "x", "a", "a", "a", "b", "y", "dd", "y"],
            printBacktrack=True,
            boolListOfList=True,
        )
        self.assertEqual(dist, 3.0)
        self. assertCountEqual(candidates, [["a", "b", "dd"]])
        # Example 10
        dist, candidates = algs_unit.longest_common_subsequence(
            ["a", "t", "b", "c", "y", "dd", "xyz"],
            ["x", "c", "x", "t", "a", "a", "a", "b", "y", "dd", "y", "xyz"],
            printBacktrack=True,
            boolListOfList=True,
        )
        self.assertEqual(dist, 5.0)
        self.assertEqual(
            candidates, [["t", "b", "y", "dd", "xyz"], ["a", "b", "y", "dd", "xyz"]]
        )

    def test_longest_common_subsequence(self):
        algs_unit = EditDistAlgs()
        # Example 1
        dist, candidates = algs_unit.longest_common_substring(
            "aa", "aa", printBacktrack=True
        )
        self.assertEqual(dist, 2)
        self.assertCountEqual(candidates, ["aa"])
        # Example 2
        dist, candidates = algs_unit.longest_common_substring(
            "aabb", "aa", printBacktrack=True
        )
        self.assertEqual(dist, 2)
        self.assertCountEqual(candidates, ["aa"])
        # Example 3
        dist, candidates = algs_unit.longest_common_substring(
            "aabbaa", "aa", printBacktrack=True
        )
        self.assertEqual(dist, 2)
        self.assertCountEqual(candidates, ["aa"])
        # Example 4
        dist, candidates = algs_unit.longest_common_substring(
            "xyxy", "yxyx", printBacktrack=True
        )
        self.assertEqual(dist, 3)
        self.assertCountEqual(candidates, ["xyx", "yxy"])
        # Example 4
        dist, candidates = algs_unit.longest_common_substring(
            "xyxy", "yxyx", printBacktrack=True
        )
        self.assertEqual(dist, 3)
        self. assertCountEqual(candidates, ["xyx", "yxy"])
        # Example 5
        dist, candidates = algs_unit.longest_common_substring(
            ["x", "y", "x", "y"], ["y", "x", "y", "x"], printBacktrack=True, boolListOfList=True
        )
        self.assertEqual(dist, 3)
        self.assertCountEqual(candidates, [["x", "y", "x"], ["y", "x", "y"]])
        # Example 6
        dist, candidates = algs_unit.longest_common_substring(
            ["a", "a", "a", "a"], ["a"], printBacktrack=True, boolListOfList=True
        )
        self.assertEqual(dist, 1)
        self.assertCountEqual(candidates, [["a"]])
        # Example 7
        dist, candidates = algs_unit.longest_common_substring(
            "x", "xxxx", printBacktrack=True
        )
        self.assertEqual(dist, 1)
        self.assertCountEqual(candidates, ["x"])


if __name__ == "__main__":
    unittest.main()
