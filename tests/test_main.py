import io
import pytest

from contextlib import redirect_stdout

from app.main import Distance


@pytest.mark.parametrize(
    'kilometers',
    [
        50,
        100,
        300,
        12.5,
        0.6
    ]
)
def test_distance_class_init(kilometers):
    distance = Distance(kilometers)
    assert distance.km == kilometers, (
        f"Instance attribute 'km' should equal to {kilometers} "
        f"when you create instance with 'Distance({kilometers})'"
    )


@pytest.mark.parametrize(
    'kilometers,output',
    [
        (50, "Distance: 50 kilometers.\n"),
        (100, "Distance: 100 kilometers.\n"),
        (300, "Distance: 300 kilometers.\n"),
        (12.5, "Distance: 12.5 kilometers.\n"),
        (0.6, "Distance: 0.6 kilometers.\n")
    ]
)
def test_distance_class_str(kilometers, output):
    distance = Distance(kilometers)
    f = io.StringIO()

    with redirect_stdout(f):
        print(distance)

    out = f.getvalue()

    assert out == output, (
        f"Output should equal to {output} "
        f"when you call 'print' with instance of Distance class"
    )


@pytest.mark.parametrize(
    'kilometers,output',
    [
        (50, "Distance(km=50)"),
        (100, "Distance(km=100)"),
        (300, "Distance(km=300)"),
        (12.5, "Distance(km=12.5)"),
        (0.6, "Distance(km=0.6)")
    ]
)
def test_distance_class_repr(kilometers, output):
    distance = Distance(kilometers)

    assert repr(distance) == output, (
        f"'repr(distance)' should equal to {output} "
        f"when distance is created with 'Distance({kilometers})'"
    )


@pytest.mark.parametrize(
    'kilometers1,kilometers2,kilometers3',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400),
        (15.5, 14.5, 30.0),
        (20.6, 40.8, 61.4)
    ]
)
def test_distance_class_add_distance_and_distance(kilometers1, kilometers2, kilometers3):
    distance1 = Distance(kilometers1)
    distance2 = Distance(kilometers2)
    distance3 = distance1 + distance2
    assert isinstance(distance3, Distance), (
        "Result of sum of Distance instances should be "
        "Distance instance"
    )
    assert distance3.km == kilometers3, (
        f"distance3.km should equal to {kilometers3}, "
        f"when 'distance3 = Distance({kilometers1}) + Distance({kilometers2})'"
    )


@pytest.mark.parametrize(
    'kilometers1,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400),
        (15.5, 14.5, 30.0),
        (20.6, 40.8, 61.4)
    ]
)
def test_distance_class_add_distance_and_number(kilometers1, kilometers2, result):
    distance1 = Distance(kilometers1)
    distance2 = distance1 + kilometers2
    assert isinstance(distance2, Distance), (
        "Result of sum of Distance instance and number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance3 = Distance({kilometers1}) + {kilometers2}'"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400),
        (15.5, 14.5, 30.0),
        (20.6, 40.8, 61.4)
    ]
)
def test_distance_class_iadd_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    instance_1 = distance1
    distance2 = Distance(kilometers2)
    distance1 += distance2
    instance_2 = distance1
    assert instance_1 is instance_2, (
        "__iadd__ should return the same instance"
    )
    assert distance1.km == result, (
        f"distance1.km should equal to {result}, "
        f"when 'distance1' is Distance({kilometers}) and "
        f"'distance1 += Distance({kilometers2})"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400),
        (15.5, 14.5, 30.0),
        (20.6, 40.8, 61.4)
    ]
)
def test_distance_class_iadd_number(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    instance_1 = distance1
    distance1 += kilometers2
    instance_2 = distance1
    assert instance_1 is instance_2, (
        "__iadd__ should return the same instance"
    )
    assert distance1.km == result, (
        f"'distance1.km' should equal to {result}, "
        f"when 'distance1' is Distance({kilometers}) and "
        f"'distance1 += {kilometers2}'"
    )


@pytest.mark.parametrize(
    'kilometers,number,result',
    [
        (50, 3, 150),
        (30, 7, 210),
        (45, 5, 225),
        (1.5, 3.0, 4.5),
        (21.4, 5.88, 125.832)
    ]
)
def test_distance_class_mul_number(kilometers, number, result):
    distance1 = Distance(kilometers)
    distance2 = distance1 * number
    assert isinstance(distance2, Distance), (
        "Result of Distance instance multiplied by number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance2 = Distance({kilometers}) * {number}'"
    )


def test_distance_class_mul_distance():
    distance1 = Distance(5)
    distance2 = Distance(3)
    try:
        result = distance1 * distance2
    except TypeError:
        pass
    else:
        assert result is None, (
            "'__mul__' method should not accept Distance instance"
        )


@pytest.mark.parametrize(
    'kilometers,number,result',
    [
        (50, 3, 16.67),
        (30, 7, 4.29),
        (45, 5, 9),
        (12.6, 3.3, 3.82),
        (26.88, 5.6, 4.8)
    ]
)
def test_distance_class_truediv_number(kilometers, number, result):
    distance1 = Distance(kilometers)
    distance2 = distance1 / number
    assert isinstance(distance2, Distance), (
        "Result of Distance instance divided by number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance2 = Distance({kilometers}) / {number}'"
    )


def test_distance_class_truediv_distance():
    distance1 = Distance(30)
    distance2 = Distance(3)
    try:
        result = distance1 / distance2
    except TypeError:
        pass
    else:
        assert result is None, (
            "'__truediv__' method should not accept Distance instance"
        )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 30, True),
        (10.2, 10.2, True),
        (20.9, 5.8, False)
    ]
)
def test_distance_class_eq_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 == distance2) is result, (
        f"'Distance({kilometers}) == Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 30, True),
        (10.2, 10.2, True),
        (20.9, 5.8, False)
    ]
)
def test_distance_class_eq_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance == kilometers2) is result, (
        f"'Distance({kilometers}) == {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False),
        (10.1, 10.1, False),
        (20.2, 5.8, True),
        (5.5, 20.9, False)
    ]
)
def test_distance_class_gt_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 > distance2) is result, (
        f"'Distance({kilometers}) > Distance{kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False),
        (10.1, 10.1, False),
        (20.2, 5.8, True),
        (5.5, 20.9, False)
    ]
)
def test_distance_class_gt_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance > kilometers2) is result, (
        f"'Distance({kilometers}) > {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False),
        (10.1, 10.1, True),
        (20.2, 5.8, True),
        (5.5, 20.9, False)
    ]
)
def test_distance_class_ge_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 >= distance2) is result, (
        f"'Distance({kilometers}) >= Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False),
        (10.1, 10.1, True),
        (20.2, 5.8, True),
        (5.5, 20.9, False)
    ]
)
def test_distance_class_ge_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance >= kilometers2) is result, (
        f"'Distance({kilometers}) >= {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True),
        (10.1, 10.1, False),
        (20.2, 5.8, False),
        (5.5, 20.9, True)
    ]
)
def test_distance_class_lt_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 < distance2) is result, (
        f"'Distance({kilometers}) < Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True),
        (10.1, 10.1, False),
        (20.2, 5.8, False),
        (5.5, 20.9, True)
    ]
)
def test_distance_class_lt_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance < kilometers2) is result, (
        f"'Distance({kilometers}) < {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True),
        (10.1, 10.1, True),
        (20.2, 5.8, False),
        (5.5, 20.9, True)
    ]
)
def test_distance_class_le_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 <= distance2) is result, (
        f"'Distance({kilometers}) <= Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True),
        (10.1, 10.1, True),
        (20.2, 5.8, False),
        (5.5, 20.9, True)
    ]
)
def test_distance_class_le_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance <= kilometers2) is result, (
        f"'Distance({kilometers}) <= {kilometers2}' should equal to {result}"
    )
