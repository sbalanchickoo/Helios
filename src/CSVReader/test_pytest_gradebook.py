import pytest
from gradebook import Gradebook, Counters


@pytest.fixture
def gb():
    Counters.init_course_id(Counters)
    gradebook = Gradebook(course_name='C1')
    return gradebook


def test_create_gradebook(gb):
    assert gb is not None
    assert 'C1' == gb.course_name


def test_gradebook_course():
    assert gb.course_ID is not None
    assert gb.course_name is not None


def test_gradebook_course_id(gb):
    assert 1 == gb.course_ID
