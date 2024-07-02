from typing import List


def _indent_patch(text: str) -> str:
    lines = text.splitlines()
    min_indent = _calculate_min_indent(lines)
    lines = [line[min_indent:] for line in lines]
    return "\n".join(lines)


def _calculate_min_indent(lines: List[str]) -> int:
    min_indent = min(
        [len(line) - len(line.lstrip()) for line in lines if line.strip() != ""]
    )
    return min_indent
