from similar_matrix import get_matrix_a, get_matrix_b
import pytest

test_data = [
    ([[1, 2], [3, -1]], [[0, 1], [2, 3]]),
]


@pytest.mark.parametrize("mat_a, mat_p", test_data)
def test_get_matrix_b(mat_a, mat_p):
    b = get_matrix_b(mat_a=mat_a, mat_p=mat_p)
    a = get_matrix_a(mat_b=b, mat_p=mat_p)
    assert a == mat_a
