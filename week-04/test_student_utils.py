import pytest
from student_utils import filter_students
from student_utils import get_student_count
from type_practice import calculate_average


# def test_filter_students():
#     students = [
#         {"name": "Tobi", "score": 90},
#         {"name": "David", "score": 85},
#         {"name": "Sarah", "score": 78},
#         {"name": "John", "score": 92},
#     ]

#     result = filter_students(students)

#     assert len(result) == 3
#     assert {"name": "Sarah", "score": 78} not in result
#     # assert filter_students(students, 90)
#     # assert filter_students([])

# def test_filter_students_custom_minimum():
#     students = [
#         {"name": "Tobi", "score": 90},
#         {"name": "David", "score": 85},
#         {"name": "Sarah", "score": 78},
#         {"name": "John", "score": 92},
#     ]

#     result = filter_students(students, 90)

#     assert len(result) == 2
#     assert {"name": "Tobi", "score": 90} in result
#     assert {"name": "John", "score": 92} in result
#     assert {"name": "David", "score": 85} not in result

# def test_filter_students_empty_list():
#     result = filter_students([])

#     assert len(result) == 0
#     assert result == []

# def test_filter_student_no_qualifiers():
#     students = [
#     {"name": "Sarah", "score": 78},
#     {"name": "David", "score": 65},
# ]
#     result = filter_students(students)
    
#     assert len(result) == 0

@pytest.fixture
def students():
    return [
        {"name": "Tobi", "score": 90},
        {"name": "David", "score": 85},
        {"name": "Sarah", "score": 78},
        {"name": "John", "score": 92},
    ]   


def test_filter_students(students):
    result = filter_students(students)

    assert len(result) == 3


def test_filter_students_custom_minimum(students):
    result = filter_students(students, 90)

    assert len(result) == 2
    assert {"name": "Tobi", "score": 90} in result
    assert {"name": "John", "score": 92} in result


@pytest.mark.parametrize(
    "minimum_score, expected_count",
    [
        (50, 4),
        (80, 3),
        (90, 2),
        (95, 0),
    ],
)
def test_filter_students_by_score(students, minimum_score, expected_count):
    result = filter_students(students, minimum_score)

    assert len(result) == expected_count

def test_get_student_count(students):
    result = get_student_count(students)

    assert result == 4

@pytest.mark.parametrize(
    "scores, expected_answer",
    [
        ([10, 20, 30], 20.0),
        ([5, 10], 7.5),
        ([8], 8.0),
    ],
)
def test_calculate_average_valid(scores: list[int], expected_answer: float):
    assert calculate_average(scores) == expected_answer


def test_calculate_average_empty_list_raises():
    with pytest.raises(ValueError, match="Scores cannot be empty"):
        calculate_average([])