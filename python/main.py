from lalilo.model import *
from lalilo.utils import ActivitiesManager


if __name__ == '__main__':
    mgr = ActivitiesManager("../activities.json")
    student = Student(Language.FR)
    # Perfect score on last activity
    activity = StudentTrace(
        activity_id=36282,
        score=1
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Not a perfect score on last activity
    activity = StudentTrace(
        activity_id=1595,
        score=0.5
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # None of the above
    activity = StudentTrace(
        activity_id=36371,
        score=0.5
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)
