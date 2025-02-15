# affix-tree

A trie-like data structure that allows storing and searching data based on the longest matching
prefix or suffix of a given string.

## Installation

```commandline
pip install affix-tree
```

## Usage

### As a prefix tree

```pycon
>>> from affix_tree import AffixTree

>>> prefix_tree: AffixTree[int] = AffixTree()
>>> prefix_tree.add('prefix', 1)
>>> prefix_tree.add('prefix-2', 2)

>>> prefix_tree.find('prefix-2-test')

2
```

### As a suffix tree

```pycon
>>> from affix_tree import AffixTree

>>> prefix_tree: AffixTree[int] = AffixTree(is_suffix_tree=True)
>>> prefix_tree.add('suffix', 1)
>>> prefix_tree.add('2-suffix', 2)

>>> prefix_tree.find('test-2-suffix')

2
```
