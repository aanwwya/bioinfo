def naive_search(sequence, pattern):
    matches = [] # # store positions where the pattern is found

    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i + len(pattern)] == pattern: # compare the pattern with the current part of the sequence
            matches.append(i) # save da matching positions

    return matches