class Counters:
    courseID = -1

    @staticmethod
    def next_course_id(self):
        if self.courseID == -1:
            self.courseID = 1
        else:
            self.courseID += 1
        return self.courseID

    @staticmethod
    def init_course_id(self):
        self.courseID = -1


class Gradebook:
    course_ID = -1
    course_name = ''

    def __init__(self, course_name):
        self.course_ID = Counters.next_course_id(Counters)
        self.course_name = course_name


