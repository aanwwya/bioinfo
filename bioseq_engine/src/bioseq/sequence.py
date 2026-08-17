class Sequence:
    """
    Immutable representation of a biological nucleotide sequence.

    The class currently supports DNA sequences and normalizes input
    into uppercase form.
    """

    VALID_BASES = frozenset("ACGT")

    def __init__(self, sequence: str):
        if not isinstance(sequence, str):
            raise TypeError("sequence must be a string")

        normalized = sequence.upper()

        if not normalized:
            raise ValueError("sequence cannot be empty")

        invalid_bases = set(normalized) - self.VALID_BASES

        if invalid_bases:
            raise ValueError(
                f"invalid DNA bases: {sorted(invalid_bases)}"
            )

        self._sequence = normalized

    @property
    def sequence(self) -> str:
        return self._sequence

    def __len__(self) -> int:
        return len(self._sequence)
    
    @property
    def length(self) -> int:
        return len(self._sequence)

    def __getitem__(self, index):
        result = self._sequence[index]

        if isinstance(index, slice):
            return Sequence(result)

        return result

    def __iter__(self):
        return iter(self._sequence)
    
    
    