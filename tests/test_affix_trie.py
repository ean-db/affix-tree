import pytest

from affix_tree import AffixTree


class TestAffixTrie:
    @pytest.mark.parametrize('trie', [AffixTree(), AffixTree(is_suffix_tree=True)])
    def test_empty_trie(self, trie: AffixTree[str]):
        assert trie.find('test') is None

    @pytest.mark.parametrize('trie', [AffixTree(), AffixTree(is_suffix_tree=True)])
    def test_duplicate_key(self, trie: AffixTree[str]):
        with pytest.raises(ValueError, match='Duplicate prefix for data: value'):
            trie.add('key', 'value')
            trie.add('key', 'value')

    @pytest.mark.parametrize('trie', [AffixTree(), AffixTree(is_suffix_tree=True)])
    def test_find_none(self, trie: AffixTree[str]):
        assert trie.find(None) is None

    @pytest.mark.parametrize('trie', [AffixTree(), AffixTree(is_suffix_tree=True)])
    def test_empty_key(self, trie: AffixTree[str]):
        with pytest.raises(ValueError, match='String is empty'):
            trie.add(None, 'value')

    def test_shorter_prefix_is_not_found(self):
        prefix_trie: AffixTree[int] = AffixTree()
        prefix_trie.add('prefix1', 1)
        prefix_trie.add('prefix2', 2)

        assert prefix_trie.find('prefix') is None

    def test_exact_prefix_is_found(self):
        prefix_trie: AffixTree[int] = AffixTree()
        prefix_trie.add('prefix1-1', 0)
        prefix_trie.add('prefix1', 1)
        prefix_trie.add('prefix2', 2)
        prefix_trie.add('prefix1-t', 3)

        assert prefix_trie.find('prefix1') == 1

    def test_longer_prefix_is_found(self):
        prefix_trie: AffixTree[int] = AffixTree()
        prefix_trie.add('prefix1', 1)
        prefix_trie.add('prefix2', 2)
        prefix_trie.add('prefix1-t', 3)

        assert prefix_trie.find('prefix1-') == 1
        assert prefix_trie.find('prefix1-test') == 3

    def test_shorter_suffix_is_not_found(self):
        suffix_trie: AffixTree[int] = AffixTree(is_suffix_tree=True)
        suffix_trie.add('1suffix', 1)
        suffix_trie.add('2suffix', 2)

        assert suffix_trie.find('suffix') is None

    def test_exact_suffix_is_found(self):
        suffix_trie: AffixTree[int] = AffixTree(is_suffix_tree=True)
        suffix_trie.add('1-1suffix', 0)
        suffix_trie.add('1suffix', 1)
        suffix_trie.add('2suffix', 2)
        suffix_trie.add('t-1suffix', 3)

        assert suffix_trie.find('1suffix') == 1

    def test_longer_suffix_is_found(self):
        suffix_trie: AffixTree[int] = AffixTree(is_suffix_tree=True)
        suffix_trie.add('1suffix', 1)
        suffix_trie.add('2suffix', 2)
        suffix_trie.add('t-1suffix', 3)

        assert suffix_trie.find('-1suffix') == 1
        assert suffix_trie.find('test-1suffix') == 3
