"""
    Edit distance algorithms:
        [x] Levenshtein edit distance
        [x] Hamming edit distance
        [ ] Damerau–Levenshtein edit distance
        [ ] Jaro–Winkler edit distance
"""

# Import relevant libraries and dependencies
from typing import List, Union, Tuple
import numpy as np
from itertools import product


class EditDistAlgs:
    """
    Class for edit distance algorithms
    """

    def __init__(
        self,
        insert_weight: int = 1.0,
        delete_weight: int = 1.0,
        match_weight: int = 0.0,
        substite_weight: int = 1.0,
    ) -> None:
        # All the weights should be non-negative.
        assert min(insert_weight, delete_weight, match_weight, substite_weight) >= 0

        # Weights of the operations
        self.insert_weight = insert_weight
        self.delete_weight = delete_weight
        self.match_weight = match_weight
        self.substite_weight = substite_weight
        self.list_of_list_separator = " ## "

    def stringlist_cartesian_product(
        self,
        lst1: Union[List[str], List[List[str]]],
        lst2: Union[List[str], List[List[str]]],
        boolListOfList: bool = False,
    ) -> Union[List[str], List[List[str]]]:
        """
        Takes the Cartesian product of two (lists of) lists of strings.
        """
        if lst1 == []:
            return lst2
        elif lst2 == []:
            return lst1
        return [
            s1 + ("" if not (boolListOfList) else self.list_of_list_separator) + s2
            for s1 in lst1
            for s2 in lst2
        ]

    def levenshtein_edit_distance(
        self, str1: Union[str, List[str]], str2: Union[str, List[str]]
    ) -> float:
        """
        Levenshtein edit distance refers to the minimum number of edit distance oeprations (insertion,
        deletion,and substitution) needed to transform one string into another.

        This function calculates the Levenshtein edit distance between two strings or (lists of strings) using dynamic programming.
        This implementation follows the original Wagner-Fischer algorithm.
            - Its time and space complexities are both quadratic (i.e., O(n x m))).
            - However, one can easily improve the space complexity and make it linear.
        """

        # Lengths of strings str1 and str2, respectively.
        n = len(str1)
        m = len(str2)

        # Initialization of the distance matrix of size (n+1) x (m+1)
        dist = np.zeros((n + 1, m + 1))
        for i in range(1, n + 1):
            dist[i, 0] = self.delete_weight * i
        for j in range(1, m + 1):
            dist[0, j] = self.insert_weight * j

        # Dynamic programming step (for the unit case where each operation has a unit cost):
        # d[i, j] := min(d[i-1, j-1] + mismatch(i, j), d[i-1, j] + 1, d[i, j-1] + 1),
        # where mismatch(i, j) is 1 if str1[i] != str2[j] and 0 otherwise.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dist[i, j] = min(
                    dist[i - 1, j - 1]
                    + (
                        self.substite_weight
                        if str1[i - 1] != str2[j - 1]
                        else self.match_weight
                    ),
                    dist[i, j - 1] + self.insert_weight,
                    dist[i - 1, j] + self.delete_weight,
                )
        return dist[n, m]

    def hamming_distance(
        self, str1: Union[str, List[str]], str2: Union[str, List[str]]
    ) -> float:
        """
        Hamming distance is equal to the number of positions at which two equal-length strings differ.
        In other words, it refers to the minimum number of substitution operations needed to transformer on string into another.
        """
        if len(str1) != len(str2):
            raise ValueError(
                "The lengths of the two strings (or lists of strings) must be equal."
            )

        dist = 0.0
        for i in range(len(str1)):
            # This is a more abstract implementation of the Hamming distance function.
            # In theory, it is possible for a match to have a cost as well.
            # For istance, we might want to penalize longer strings.
            dist += self.match_weight if str1[i] == str2[i] else self.substite_weight
        return dist

    def longest_common_subsequence(
        self,
        str1: Union[str, List[str]],
        str2: Union[str, List[str]],
        printBacktrack: bool = False,
        boolListOfList: bool = False,
    ) -> Tuple[float, Union[List[str], List[List[str]]]]:
        """
        Longest common subsequence (LCSubseq) of two strings (or lists of strings) is a subsequence of maximal length that appears in both of them.
        - Not that a common subsequence is a sequence that appears in both strings in some increasing order, but not necessarily contigious.

        linear space solution.
        """
        # Lengths of strings str1 and str2, respectively.
        n = len(str1)
        m = len(str2)

        # Initialization of the matrix d of size (n+1) x (m+1)
        d = np.zeros((n + 1, m + 1))
        # Normally need to initialize d[i, j] = 0 for i =0 or j = 0
        # But that is already taken care of under this implementation since we initialize the matrix with all 0's.

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    d[i, j] = d[i - 1, j - 1] + 1
                else:
                    d[i, j] = max(d[i - 1, j], d[i, j - 1])

        def backtrack(i: int, j: int) -> Union[List[str], List[List[str]]]:
            """
            Given the matrix d, backtracks and prints all the longest subsequences.
            """
            if i == 0 or j == 0:
                return [""] if not (boolListOfList) else []
            if str1[i - 1] == str2[j - 1]:
                insert_elt = str1[i - 1] if not (boolListOfList) else [str1[i - 1]]
                final = list(
                    set(
                        self.stringlist_cartesian_product(
                            backtrack(i - 1, j - 1),
                            insert_elt,
                            boolListOfList=boolListOfList,
                        )
                    )
                )
                return final

            rest = []
            if d[i, j - 1] >= d[i - 1, j]:
                rest = backtrack(i, j - 1)
            if d[i - 1, j] >= d[i, j - 1]:
                rest += backtrack(i - 1, j)
            return list(set(rest))

        lcs_candidates = None
        if printBacktrack:
            lcs_candidates = backtrack(n, m)
            if boolListOfList and lcs_candidates:
                lcs_candidates = [
                    elt.split(self.list_of_list_separator) for elt in lcs_candidates
                ]
        return d[n, m], lcs_candidates
