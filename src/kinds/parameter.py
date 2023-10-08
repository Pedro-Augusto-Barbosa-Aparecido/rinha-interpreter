from src.kinds.location import Location


class Parameter:
    def __init__(self, text: str, location: Location):
        self._text = text
        self._location = location

    @property
    def text(self) -> str:
        return self._text

    @property
    def location(self) -> Location:
        return self._location
