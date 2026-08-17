import timeit

from bioseq_engine.src.bioseq.search import naive_search
from bioseq_engine.src.bioseq.kmp import kmp_search


def benchmark_search(
    search_function,
    sequence,
    pattern,
    iterations,
    repeats=5
):
    timings = timeit.repeat(
        lambda: search_function(sequence, pattern),
        number=iterations,
        repeat=repeats
    )

    return timings


sequence_sizes = [1000, 10000, 100000]

patterns = {
    "existing": "ATGCGATCGATGCTAGATGCGATC",
    "short": "ATG",
    "missing": "GGGGGGGGGGGGGGGGGGGG",
}


for size in sequence_sizes:
    sequence = "ATGCGATCGATGCTAG" * size
    iterations = max(1, 100000 // size)

    for pattern_name, pattern in patterns.items():

        # Both implementations must return identical results.
        assert naive_search(sequence, pattern) == kmp_search(
            sequence,
            pattern
        )

        naive_timings = benchmark_search(
            naive_search,
            sequence,
            pattern,
            iterations
        )

        kmp_timings = benchmark_search(
            kmp_search,
            sequence,
            pattern,
            iterations
        )

        naive_min = min(naive_timings) / iterations
        kmp_min = min(kmp_timings) / iterations

        naive_median = (
            sorted(naive_timings)[len(naive_timings) // 2]
            / iterations
        )

        kmp_median = (
            sorted(kmp_timings)[len(kmp_timings) // 2]
            / iterations
        )

        speedup = naive_median / kmp_median

        print(f"pattern: {pattern_name}")
        print(f"sequence size: {len(sequence)}")
        print(f"iterations: {iterations}")

        print(f"naive min: {naive_min:.6f} seconds")
        print(f"naive median: {naive_median:.6f} seconds")

        print(f"kmp min: {kmp_min:.6f} seconds")
        print(f"kmp median: {kmp_median:.6f} seconds")

        print(f"speedup (naive/kmp): {speedup:.2f}x")
        print()