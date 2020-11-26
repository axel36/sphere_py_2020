"""lru"""
import typing as tp


class LRUCache:
    """lru"""

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise Exception("capacity must be > 0")
        self._capacity = capacity
        self._storage = {}
        self._keys = []

    def get(self, key: str) -> tp.Optional[str]:
        """get key"""
        if key in self._storage:
            self._move_to_recent(key)
            return self._storage[key]

        return None

    def set(self, key: str, value: str) -> None:
        """set to cache"""
        if key in self._storage:
            self._storage[key] = value
            self._move_to_recent(key)
            return

        if self._capacity == len(self._keys):
            self.delete(self._keys[0])

        self._keys.append(key)
        self._storage[key] = value

    def delete(self, key: str) -> None:
        """delete from cache"""
        if key not in self._storage:
            return

        self._keys.remove(key)
        self._storage.pop(key)

    def _move_to_recent(self, key: str) -> None:
        """move to recent"""
        self._keys.remove(key)
        self._keys.append(key)
