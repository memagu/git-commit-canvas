from typing import Generator

from charachter_maps import CharacterMap


class Canvas:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._data = [[0] * self.width for _ in range(self.height)]

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def ensure_inside(self, x, y) -> None:
        if not self.is_inside(x, y):
            raise ValueError("x or y is not inside the canvas")

    def set_pixel(self, x: int, y: int, weight: int = 1) -> None:
        self.ensure_inside(x, y)
        self._data[y][x] = weight

    def set_character(self, x: int, y: int, character: str, character_map: CharacterMap, weight: int = 1) -> None:
        if len(character) != 1:
            raise ValueError(f"\"{character}\" is not a character")
        if character not in character_map:
            raise ValueError(f"There is no mapping for: \"{character}\"")

        for dy, row in enumerate(character_map[character]):
            for dx, value in enumerate(row):
                self.set_pixel(x + dx, y + dy, value * weight)

    def set_string(self, x: int, y: int, string: str, character_map: CharacterMap, spacing: int = 1, ignore_errors: bool = False) -> None:
        dx = 0
        for character in string:
            try:
                self.set_character(x + dx, y, character, character_map)
            except ValueError as e:
                if not ignore_errors:
                    raise e
            dx += len(character_map[character][0]) + spacing

    def get_pixel(self, x: int, y: int) -> int:
        self.ensure_inside(x, y)
        return self._data[y][x]

    def get_pixels(self) -> Generator[tuple[int, int, int], None, None]:
        for y, row in enumerate(self._data):
            for x, weight in enumerate(row):
                yield x, y, weight
