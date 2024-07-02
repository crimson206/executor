from typing import overload, List, Union, Dict, Any, Optional
from .util import _indent_patch


@overload
def exec_with_namespace(
    code: str,
    namespace: Dict[str, Any],
    globals: Optional[Dict[str, Any]] = None,
    indent_patch: bool = True,
) -> None:
    """Run a single code string."""
    ...


@overload
def exec_with_namespace(
    codes: List[str],
    namespace: Dict[str, Any],
    globals: Optional[Dict[str, Any]] = None,
    indent_patch: bool = True,
) -> None:
    """Run multiple code strings."""
    ...


def exec_with_namespace(
    code: Union[str, List[str]],
    namespace: Dict[str, Any],
    globals: Optional[Dict[str, Any]] = None,
    indent_patch: bool = True,
) -> None:
    if globals is None:
        globals = {}

    if isinstance(code, str):
        _exec_with_namespace(code, namespace, globals, indent_patch)
    elif isinstance(code, list):
        for single_code in code:
            _exec_with_namespace(single_code, namespace, globals, indent_patch)
    else:
        raise TypeError("code must be a string or a list of strings")


def _exec_with_namespace(
    code: str,
    namespace: Dict[str, Any],
    globals: Dict[str, Any],
    indent_patch: bool = True,
) -> None:
    if indent_patch:
        code = _indent_patch(code)
    exec(code, globals, namespace)
