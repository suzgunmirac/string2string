# String to String Algorithms

### Edit distance:
    - [x] Levenshtein edit distance
        - [x] Wagner–Fischer (WF) algorithm: O(nm) time and O(nm) space
            - [ ] Efficient version of WF: O(nm) time and O(min(n,m)) space
    - [x] Hamming edit distance
        - Naive solution: O(n) time and O(1) space
    - [x] Damerau–Levenshtein edit distance
    - [x] Jaccard distance

### Alignment / Similarity:
    - [x] Longest common substring
    - [x] Longest common subsequence
    - [x] Jaccard similarity
    - [ ] Sequence alignment
        - [ ] Smith-Waterman algorithm (local): O(nm) time and O(nm) space
        - [ ] Needleman–Wunsch algorithm (global): O(nm) time and O(nm) space
            - [ ] Hirschberg's algorithm: O(nm) time and O(min(n,m)) space
    - [ ] Dynamic time warping (DTW)

### Search:
    - [ ] Single string search:
        - [ ] Rabin-Karp algorithm
        - [ ] Knuth-Morris-Pratt algorithm
        - [ ] Boyer-Moore algorithm
        - [ ] Two-way string-matching algorithm