"""
Main file - basic code to test ruff and mypy.

if x then:
call_func()
"""


def foo() -> None:
    print("foo")


MY_LIST = [
    "Jane",
    "John",
    "Joe",
    "Jill",
]

MY_DICT = {"key": "value", "key2": "value2", "key3": "value3"}

long_string = (
    "This is a very long line that exceeds the maximum allowed line length for \
    Python code. This is a very long line that exceeds the \
    maximum allowed"
)

MY_TUPLE = (1, 2, 3)
