"""
    Edit distance algorithms:
        [x] Levenshtein edit distance
        [ ] Hamming edit distance
        [ ] Damerau–Levenshtein edit distance
        [ ] Jaro–Winkler edit distance
"""

# Import relevant libraries and dependencies
import numpy as np


class EditDistAlgs:
    """
        Class for edit distance algorithms
    """
    
    def __init__(self, insert_weight: int = 1., delete_weight: int = 1., match_weight: int = 0., substite_weight: int = 1.) -> None:
        # All the weights should be non-negative.
        assert min(insert_weight, delete_weight, match_weight, substite_weight) >= 0

        # Weights of the operations
        self.insert_weight = insert_weight
        self.delete_weight = delete_weight
        self.match_weight = match_weight
        self.substite_weight = substite_weight


    def levenshtein_edit_distance(self, str1: str, str2: str) -> float:
        """
            Levenshtein edit distance refers to the minimum number of edit distance oeprations (insertion, 
            deletion,and substitution) needed to transform one string into another.

            This function calculates the Levenshtein edit distance between two strings using dynamic programming.
            This implementation follows the original Wagner-Fischer algorithm.
                - Its time and space complexities are both quadratic (i.e., O(n x m))).
                - However, one can easily improve the space complexity and make it linear.
        """

        # Lengths of strings str1 and str2, respectively.
        n = len(str1)
        m = len(str2)

        # Initialization of the distance matrix of size (n+1) x (m+1)
        dist = np.zeros((n+1, m+1))
        for i in range(1, n+1):
            dist[i, 0] = self.delete_weight * i
        for j in range(1, m+1):
            dist[0, j] = self.insert_weight * j
        
        # Dynamic programming step (for the unit case where each operation has a unit cost):
        # d[i, j] := min(d[i-1, j-1] + mismatch(i, j), d[i-1, j] + 1, d[i, j-1] + 1),
        # where mismatch(i, j) is 1 if str1[i] != str2[j] and 0 otherwise.
        for i in range(1, n+1):
            for j in range(1, m+1):
                dist[i, j] = min(
                    dist[i-1, j-1] + (self.substite_weight if str1[i-1] != str2[j-1] else self.match_weight),
                    dist[i, j-1] + self.insert_weight,
                    dist[i-1, j] + self.delete_weight
                )
        return dist[n, m]