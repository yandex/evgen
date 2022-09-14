from abc import abstractmethod
from itertools import chain
from typing import List, Optional, Protocol, Union

from evgen.code_generators import code as evgen_code

TAB = " " * 4


class Statement(Protocol):
    def lines(self) -> List[str]:
        ...


def _flatten_list_statements(statements: List[Statement]) -> List[str]:
    lines = list(chain.from_iterable([statement.lines() for statement in statements]))
    lines = [f"{TAB}{line}" for line in lines]
    return lines


class TxtDoc:
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def lines(self) -> List[str]:
        lines = list(
            chain.from_iterable([statement.lines() for statement in self.statements])
        )
        lines = [f"{line}" for line in lines]
        return lines


class MarkdownDoc:
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def lines(self) -> List[str]:
        lines = list(
            chain.from_iterable([statement.lines() for statement in self.statements])
        )
        lines = [f"{TAB}{line}" for line in lines]
        return ["/**"] + lines + ["*/"]


class Line:
    def __init__(self, line: str):
        self.line = line

    def lines(self) -> List[str]:
        return [self.line]


class EmptyLine:
    def lines(self) -> List[str]:
        return [""]


class Block:
    def __init__(self, statements: List[Statement]):
        self._statements = statements

    def lines(self) -> List[str]:
        return list(
            chain.from_iterable([statement.lines() for statement in self._statements])
        )


class ClosureSymbol(Protocol):
    @property
    @abstractmethod
    def start_symbol(self) -> str:
        ...

    @property
    @abstractmethod
    def end_symbol(self) -> str:
        ...


class EmptyBracket:
    def __init__(self):
        self._start_symbol = ""
        self._end_symbol = ""

    @property
    def start_symbol(self) -> str:
        return self._start_symbol

    @property
    def end_symbol(self) -> str:
        return self._end_symbol


class CurveBracket:
    def __init__(self):
        self._start_symbol = "{"
        self._end_symbol = "}"

    @property
    def start_symbol(self) -> str:
        return self._start_symbol

    @property
    def end_symbol(self) -> str:
        return self._end_symbol


class RoundBracket:
    def __init__(self):
        self._start_symbol = "("
        self._end_symbol = ")"

    @property
    def start_symbol(self) -> str:
        return self._start_symbol

    @property
    def end_symbol(self) -> str:
        return self._end_symbol


class Closure:
    def __init__(
        self,
        header: Union[str, Statement],
        statements: List[Statement],
        closure_symbol: ClosureSymbol = CurveBracket(),
        postfix: Optional[str] = None,
    ):
        self._header = header
        self._statements = statements
        self._closure_symbol = closure_symbol
        self._postfix = postfix

    def lines(self) -> List[str]:
        if isinstance(self._header, str):
            header = [self._header + " " + self._closure_symbol.start_symbol]
        else:
            header = self._header.lines() + [self._closure_symbol.start_symbol]
        lines = _flatten_list_statements(self._statements)
        end_symbol = self._closure_symbol.end_symbol
        end_symbol += self._postfix if self._postfix else ""
        lines = header + lines + [end_symbol]
        return lines


class Case:
    def __init__(self, header: str, statements: List[Statement]):
        self._header = header
        self._statements = statements

    def lines(self) -> List[str]:
        lines = _flatten_list_statements(self._statements)
        lines = [self._header] + lines
        return lines


class Switch:
    def __init__(self, header: str, cases: List[Case]):
        self._header = header
        self._cases = cases

    def lines(self) -> List[str]:
        lines = list(
            chain.from_iterable([statement.lines() for statement in self._cases])
        )
        lines = [self._header + " {"] + lines + ["}"]
        return lines


class IfElse:
    def __init__(
        self,
        header: str,
        if_statements: List[Statement],
        else_statements: List[Statement],
    ):
        self._header = header
        self._if_statements = if_statements
        self._else_statements = else_statements

    def lines(self) -> List[str]:

        if_lines = list(
            chain.from_iterable(
                [statement.lines() for statement in self._if_statements]
            )
        )
        if_lines = [f"{TAB}{line}" for line in if_lines]

        else_lines = list(
            chain.from_iterable(
                [statement.lines() for statement in self._else_statements]
            )
        )
        else_lines = [f"{TAB}{line}" for line in else_lines]

        lines = [self._header + " {"] + if_lines + ["} else {"] + else_lines + ["}"]
        return lines


class Enum(Protocol):
    @staticmethod
    def create(name: str, values: List[str], prefix: Optional[str] = None):
        ...

    @property
    def name(self) -> str:
        ...

    def lines(self) -> List[str]:
        ...


class EventFunctionSerializer(Protocol):
    def get_event_function_enums(
        self, function: evgen_code.Function
    ) -> List[Statement]:
        ...

    def get_event_function_header(
        self, function: evgen_code.Function
    ) -> Union[str, Statement]:
        ...

    def get_event_function_statements(
        self, function: evgen_code.Function
    ) -> List[Statement]:
        ...

    def get_event_function_doc(self, doc: evgen_code.Doc) -> Statement:
        ...

    def get_event_function_param_structure(
        self, function: evgen_code.Function
    ) -> List[Statement]:
        ...


class EventFunction:
    def __init__(
        self, function: evgen_code.Function, serializer: EventFunctionSerializer
    ):
        self._function = function
        self._serializer = serializer

    def lines(self) -> List[str]:
        event_function_statements = list()
        event_function_statements.extend(
            self._serializer.get_event_function_enums(self._function)
        )
        event_function_statements.append(
            self._serializer.get_event_function_doc(self._function.doc)
        )
        event_function_statements.extend(
            self._serializer.get_event_function_param_structure(self._function)
        )
        header = self._serializer.get_event_function_header(self._function)
        statements = self._serializer.get_event_function_statements(self._function)
        function_statement = Closure(header=header, statements=statements)
        event_function_statements.append(function_statement)
        event_function_statements.append(EmptyLine())
        event_function_lines = list()
        for statement in event_function_statements:
            event_function_lines.extend(statement.lines())
        return event_function_lines
