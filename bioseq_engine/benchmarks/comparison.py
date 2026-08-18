from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    motif_count: int
    kmp_time: float
    aho_corasick_time: float

    @property
    def speedup(self) -> float:
        return self.kmp_time / self.aho_corasick_time


def print_comparison(results: list[BenchmarkResult]) -> None:
    print()
    print("Motifs | KMP (s) | Aho-Corasick (s) | Speedup")
    print("-" * 50)

    for result in results:
        print(
            f"{result.motif_count:6d} | "
            f"{result.kmp_time:7.2f} | "
            f"{result.aho_corasick_time:16.2f} | "
            f"{result.speedup:6.2f}x"
        )