def test_comparison_1():
    assert ("home", "work") == ("home", "work")


def test_comparison_2():
    assert "QA" == "QA"


def test_comparison_3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
