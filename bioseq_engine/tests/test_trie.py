from bioseq_engine.src.bioseq.trie import TrieNode, Trie


def test_trie_node():
    node = TrieNode()

    assert node.children == {}
    assert node.is_end is False
    assert node.patterns == []


def test_trie_insert():
    trie = Trie()

    trie.insert("ATG")

    assert "A" in trie.root.children

    node_a = trie.root.children["A"]
    assert "T" in node_a.children

    node_t = node_a.children["T"]
    assert "G" in node_t.children

    node_g = node_t.children["G"]

    assert node_g.is_end is True
    assert node_g.patterns == ["ATG"]


def test_trie_shared_prefix():
    trie = Trie()

    trie.insert("ATG")
    trie.insert("ATC")

    node_a = trie.root.children["A"]
    node_t = node_a.children["T"]

    assert "G" in node_t.children
    assert "C" in node_t.children

    assert node_t.children["G"].patterns == ["ATG"]
    assert node_t.children["C"].patterns == ["ATC"]
    
    
def test_build_failure_links():
    trie = Trie()

    trie.insert("ATG")
    trie.insert("TGA")

    trie.build_failure_links()

    node_a = trie.root.children["A"]
    node_at = node_a.children["T"]
    node_atg = node_at.children["G"]

    node_t = trie.root.children["T"]
    node_tg = node_t.children["G"]

    assert node_a.fail is trie.root
    assert node_t.fail is trie.root
    assert node_at.fail is node_t
    assert node_atg.fail is node_tg
    
    
def test_trie_search():
    trie = Trie()

    trie.insert("ATG")
    trie.insert("TGA")

    results = trie.search("ATGA")

    assert sorted(results) == [
        (0, "ATG"),
        (1, "TGA"),
    ]
    
def test_trie_search_overlapping():
    trie = Trie()

    trie.insert("ATG")
    trie.insert("TGA")

    results = trie.search("ATGA")

    assert sorted(results) == [
        (0, "ATG"),
        (1, "TGA"),
    ]