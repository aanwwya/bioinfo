from collections import deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.patterns = []
        self.fail = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root

        for base in pattern:
            if base not in node.children:
                node.children[base] = TrieNode()

            node = node.children[base]

        node.is_end = True
        node.patterns.append(pattern)

    def build_failure_links(self):
        queue = deque()

        self.root.fail = self.root

        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            current = queue.popleft()

            for base, child in current.children.items():
                queue.append(child)

                failure = current.fail

                while (
                    failure is not self.root
                    and base not in failure.children
                ):
                    failure = failure.fail

                if base in failure.children:
                    child.fail = failure.children[base]
                else:
                    child.fail = self.root

    def search(self, sequence):
        self.build_failure_links()

        results = []

        node = self.root

        for index, base in enumerate(sequence):
            while node is not self.root and base not in node.children:
                node = node.fail

            if base in node.children:
                node = node.children[base]
            else:
                node = self.root

            current = node

            while current is not self.root:
                for pattern in current.patterns:
                    results.append(
                        (index - len(pattern) + 1, pattern)
                    )

                current = current.fail

        return results