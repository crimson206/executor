import pytest
from crimson.executor import exec_with_namespace


script_var = 0
LOCALS = locals()


"""
exec_with_namespace(code, namespace) = exec(code, namespace, namespace)
exec_with_namespace(code, namespace, globals()) = exec(code, globals(), namespace)
"""


def test_function_locals_not_include_script_var():
    with pytest.raises(NameError):
        exec_with_namespace("script_var", locals())


def test_globals_in_function_not_include_script_var():
    exec_with_namespace("assert script_var == 0", globals())


def test_locals_in_script_is_globals():
    assert LOCALS == globals()


def test_globals_not_pass_function_var():
    function_var = 0
    with pytest.raises(NameError):
        exec_with_namespace("assert function_var == 0", globals())


def test_mock_func_env_meaning_function_var_and_script_var():
    function_var = 0

    exec_with_namespace(
        "assert function_var == 0 \nassert script_var == 0", locals(), globals()
    )


def test_generate_variables():
    namespaces = {}

    exec_with_namespace(
        "a, b, c = 1, 2, 3", namespaces
    )

    assert namespaces['a'] == 1
    assert len(namespaces) == 3


def test_execute_multi_codes():
    codes = [
        "a = 1",
        "b = 2",
    ]

    namespaces = {}

    exec_with_namespace(
        codes, namespaces
    )

    assert namespaces['a'] == 1
    assert namespaces['b'] == 2


def test_indent_patch_not_applied():
    code = """
    a = 1
    b = 2
    """

    namespaces = {}

    exec_with_namespace(
        code, namespaces
    )

    assert namespaces['a'] == 1
    assert namespaces['b'] == 2


if __name__ == "__main__":
    pytest.main([__file__])
