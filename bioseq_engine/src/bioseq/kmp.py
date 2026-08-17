def build_lps(pattern):
    lps = [0] * len(pattern)  # stores the longest prefix suffix length for each position
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(sequence, pattern):
    if not pattern:
        return []

    lps = build_lps(pattern)  # preprocess the pattern before searching
    matches = []

    i = 0
    j = 0

    while i < len(sequence):
        if sequence[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                matches.append(i - j)  # record the starting index of a match
                j = lps[j - 1]  # reuse the matched prefix for overlapping matches

        elif j > 0:
            j = lps[j - 1]  # skip comparisons using previously matched characters

        else:
            i += 1

    return matches