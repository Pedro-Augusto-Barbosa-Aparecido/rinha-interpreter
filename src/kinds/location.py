class Location:
    def __init__(self, start: int, end: int, filename: str):
        self._start = start
        self._end = end

        self._filename = filename

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

    @property
    def filename(self) -> str:
        return self._filename
