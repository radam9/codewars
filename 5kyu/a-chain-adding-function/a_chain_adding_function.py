import pytest

def solution(input_: str) -> int:
    # Implementation
    pass

INPUT = ""
EXPECTED = ""

@pytest.mark.parametrize(
    ("input_", "expected"),
    ((INPUT, EXPECTED),),
)
def test(input_: str, expected: int) -> None:
    output = solution(input_)
    assert output == expected, "Wrong answer!"
