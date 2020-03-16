from lalilo.model import *
from lalilo.utils import ActivitiesManager


if __name__ == '__main__':
    mgr = ActivitiesManager("../activities.json")
    student = Student(Language.FR)
    # Perfect score on last activity
    # returns next of different type
    activity = StudentTrace(
        activity_id=36312,
        score=1
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Perfect score on last activity and no next of different type
    # just returns next
    activity = StudentTrace(
        activity_id=309366,
        score=1
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Not a perfect score on last activity
    # return next lower level of different type
    activity = StudentTrace(
        activity_id=1595,
        score=0.5
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # None of the above (level 0 activity)
    activity = StudentTrace(
        activity_id=36371,
        score=0.5
    )
    student.traces = [activity]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)
