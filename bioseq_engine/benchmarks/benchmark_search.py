import time

from bioseq_engine.src.bioseq.search import naive_search


sequence = "ATGCGATCGATGCTAG" * 1000
pattern = "ATG"

start = time.perf_counter()

for _ in range(100):
    naive_search(sequence, pattern)

end = time.perf_counter()

print("time:", end - start, "seconds")