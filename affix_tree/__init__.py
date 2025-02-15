from typing import Optional, Iterator


class AffixTree[T]:
    """
    A trie-like data structure that allows storing and searching data based on the longest matching
    prefix or suffix of a given string.
    """
    __slots__ = ['_data', '_prefixes', '_is_suffix_tree']

    def __init__(self, *, is_suffix_tree: bool = False):
        """
        Initializes an AffixTree instance.

        Args:
            is_suffix_tree (bool): If True, constructs a suffix tree; otherwise, constructs a prefix tree.
        """
        self._data: Optional[T] = None
        self._prefixes: dict[str, AffixTree] = {}
        self._is_suffix_tree = is_suffix_tree

    def add(self, key: str, data: T):
        """
        Adds a prefix (or suffix) with an associated value to the tree.

        Args:
            key (str): The key (prefix or suffix) to be inserted.
            data (T): The data to be associated with the key.

        Raises:
            ValueError: If the key is empty or if the key already exists with a different value.
        """
        if not key:
            raise ValueError('String is empty')

        prefixes = self._prefixes

        for s, is_last in self._iterate_string(key):
            if is_last:
                if s in prefixes and prefixes[s]._data is not None:
                    raise ValueError(f'Duplicate prefix for data: {data}')

                if s not in prefixes:
                    prefixes[s] = AffixTree(is_suffix_tree=self._is_suffix_tree)

                prefixes[s]._data = data
            else:
                if s not in prefixes:
                    prefixes[s] = AffixTree(is_suffix_tree=self._is_suffix_tree)

                prefixes = prefixes[s]._prefixes

    def find(self, string: str) -> Optional[T]:
        """
        Finds the data associated with a longest prefix or suffix of a given string.

        Args:
            string (str): The string to search for.

        Returns:
            Optional[T]: The best-matching data, or None if no match is found.
        """
        if not string:
            return None

        prefixes = self._prefixes
        best_match = None

        for s, _ in self._iterate_string(string):
            if s not in prefixes:
                return best_match

            if prefixes[s]._data is not None:
                best_match = prefixes[s]._data

            prefixes = prefixes[s]._prefixes

        return best_match

    def _iterate_string(self, string: str) -> Iterator[tuple[str, bool]]:
        start, end = (len(string) - 1, -1) if self._is_suffix_tree else (0, len(string))
        step = -1 if self._is_suffix_tree else 1
        yield from ((string[i], i == end - step) for i in range(start, end, step))
