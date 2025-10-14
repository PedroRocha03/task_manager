from typing import Any

class InMemoryStorage:
    def __init__(self):
        self._data: dict = {}

    def add(self, id: int, item: Any):
        self._data[id] = item

    def get(self, id: int) -> Any | None:
        return self._data.get(id)

    def get_all(self) -> list[Any]:
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self):
        self._data.clear()