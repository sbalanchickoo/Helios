import unittest
from gradebook import Gradebook, Counters


class GradebookTest(unittest.TestCase):

    def test_create_gradebook(self):
        Counters.init_course_id(Counters)
        gradebook = Gradebook(course_name='C1')
        self.assertIsNotNone(gradebook)

    def test_gradebook_course(self):
        Counters.init_course_id(Counters)
        gradebook = Gradebook(course_name='C1')
        self.assertIsNotNone(gradebook.course_ID)
        self.assertIsNotNone(gradebook.course_name)

    def test_gradebook_courseID(self):
        Counters.init_course_id(Counters)
        gradebook = Gradebook('C1')
        self.assertEqual(1, gradebook.course_ID)
