def build_lps(pattern):
    pattern_length = len(pattern)

    lps = [0] * pattern_length
    length = 0
    i = 1

    while i < pattern_length:
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

    sequence_length = len(sequence)
    pattern_length = len(pattern)

    lps = build_lps(pattern)
    matches = []

    i = 0
    j = 0

    while i < sequence_length:
        if sequence[i] == pattern[j]:
            i += 1
            j += 1

            if j == pattern_length:
                matches.append(i - j)
                j = lps[j - 1]

        elif j > 0:
            j = lps[j - 1]

        else:
            i += 1

    return matches