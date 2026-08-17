from bioseq_engine.src.bioseq.sequence import Sequence


class FastaRecord:
    def __init__(
        self,
        record_id: str,
        sequence: Sequence,
        description: str = "",
    ):
        if not record_id:
            raise ValueError("record_id cannot be empty")

        self.record_id = record_id
        self.sequence = sequence
        self.description = description

    def __repr__(self):
        return (
            f"FastaRecord("
            f"record_id={self.record_id!r}, "
            f"sequence_length={len(self.sequence)}, "
            f"description={self.description!r}"
            f")"
        )