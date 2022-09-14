from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Union

from evgen.event_parser import types as parser_types


class Node:
    def __init__(self):
        self.namespaces: parser_types.NamespaceList[
            parser_types.EventVersion
        ] = parser_types.NamespaceList[parser_types.EventVersion](list())
        self.dirs: Dict[str, Node] = dict()


@dataclass
class Header:
    level: int
    text: str


DocElement = Union[Header, parser_types.Namespace[parser_types.EventVersion]]


class MonoDocIterator:
    def __init__(self, root_node: Node):
        self._elements = self._get_chapters(root_node)
        self.counter = 0

    def _get_chapters(
        self,
        node: Node,
        header_level: int = 0,
        doc_elements: Optional[DocElement] = None,
    ) -> List[DocElement]:
        if doc_elements is None:
            doc_elements = list()

        for dir_name, sub_node in node.dirs.items():
            doc_elements.append(Header(level=header_level, text=dir_name))
            self._get_chapters(
                sub_node, header_level=header_level + 1, doc_elements=doc_elements
            )

        for namespace in node.namespaces:
            doc_elements.append(Header(level=header_level, text=namespace.name))
            doc_elements.append(namespace)
        return doc_elements

    def __next__(self) -> DocElement:
        if self.counter == len(self._elements):
            raise StopIteration
        chapter = self._elements[self.counter]
        self.counter += 1
        return chapter


class MonoDoc:
    def __init__(
        self,
        namespace_list: parser_types.NamespaceList[parser_types.EventVersionObject],
    ):
        self.namespace_list = namespace_list
        self.root_node = self._create()

    def _create(self) -> Node:
        mono_doc = Node()
        for namespace in self.namespace_list:
            if namespace.documentation_dir is None:
                mono_doc.namespaces.append(namespace)
            else:
                doc_dir = Path(namespace.documentation_dir)
                current_level = self._find_node(mono_doc, doc_dir)
                current_level.namespaces.append(namespace)
        return mono_doc

    def _find_node(self, node: Node, path: Path) -> Node:
        parents = path.parents

        if len(parents) == 1:
            if path.name not in node.dirs:
                node.dirs[path.name] = Node()
            return node.dirs[path.name]

        parent = list(path.parents)[0].as_posix()
        if parent not in node.dirs:
            node.dirs[parent] = Node()

        path = path.relative_to(parent)
        return self._find_node(node.dirs[parent], path)

    def __iter__(self):
        return MonoDocIterator(self.root_node)
