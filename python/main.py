from lalilo.model import *
from lalilo.utils import ActivitiesManager


if __name__ == '__main__':
    mgr = ActivitiesManager("../activities.json")
    student = Student(Language.FR, True)
    # Perfect score on last activity
    # returns next of different type
    student.traces = [
        StudentTrace(activity_id=36312, score=1)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Perfect score on last activity and no next of different type
    # just returns next
    student.traces = [
        StudentTrace(activity_id=309366, score=1)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Not a perfect score on last activity
    # return next lower level of different type
    student.traces = [
        StudentTrace(activity_id=1595, score=0.5)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # None of the above (level 0 activity)
    student.traces = [
        StudentTrace(activity_id=36371, score=0.5)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)
    
    # Student got a discovery activity
    # Next activity is on the same skill
    student.traces = [
        StudentTrace(activity_id=36354, score=1)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

    # Student without microphone
    # reading activity not suggested
    student.microphone = False
    student.traces = [
        StudentTrace(activity_id=16, score=1)
    ]
    suggested = mgr.get_most_relevant_activity(student)
    print(suggested.__dict__)

