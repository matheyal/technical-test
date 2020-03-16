import json
from collections import defaultdict
from typing import List, Dict
from lalilo.model import *


class ActivitiesManager():
    """
    Loads activities and offers method to manipulate them
    """
    DISCOVERY_TYPES = ("discovery_generativity",
                       "discovery_grapheme_to_phoneme", "discovery_sight_word")

    def __init__(self, activities_file: str):
        with open(activities_file, "r") as fp:
            self.activities: List[Activity] = json.load(
                fp, object_hook=Activity.from_json)
            # Group activities by language
            self.activities_by_language: Dict[Language,
                                              List[Activity]] = defaultdict(list)
            for a in self.activities:
                self.activities_by_language[a.language].append(a)
            print(f"Loaded {len(self.activities)} activities")
            print(
                f"{len(self.activities_by_language[Language.EN.name])} EN activities")
            print(
                f"{len(self.activities_by_language[Language.FR.name])} FR activities")

    def get_most_relevant_activity(self, student: Student) -> Activity:
        if student.traces == None or len(student.traces) == 0:
            return self.activities_by_language[student.language.name][0]

        last_activity: Activity = self.get_activity(
            student.traces[0].activity_id, student.language)
        next_activity = None
        # If last activity was a discovery, we give the student an activity on the same skill
        if last_activity.exercise_type in ActivitiesManager.DISCOVERY_TYPES:
            next_activity = self.get_activity_with_skill(
                last_activity, student.language, student.microphone)

        # If perfect score on last activity
        if next_activity is None and student.traces[0].score == 1.0:
            next_activity = self.get_next_activity(
                last_activity, student.language, student.microphone)
        elif student.traces[0].score != 1.0:
            next_activity = self.get_lower_level_activity(
                last_activity, student.language, student.microphone)

        if next_activity is not None:
            # Check if the proposed activity is a new skill
            # If so, propose a discovery instead
            if self.student_has_skill(student, next_activity.skill):
                return next_activity
            discovery = self.get_discovery(
                next_activity.skill, student.language)
            if discovery is not None:
                return discovery
            return next_activity
        return last_activity

    def get_next_activity(self, activity: Activity, language: Language = None, microphone: bool = True) -> Activity:
        activities = self.get_activities(microphone, language)
        # Find index of activity in list
        for i in range(len(activities)):
            a = activities[i]
            if a.id == activity.id:
                activity_idx = i
                break
        # Find next activity of different type
        for i in range(activity_idx + 1, len(activities)):
            a = activities[i]
            if a.exercise_type != activity.exercise_type:
                return a
        # If no different type found, just return next
        if activity_idx is not None and activity_idx < len(activities) - 1:
            return activities[activity_idx+1]
        return None

    def get_activity_with_skill(self, activity: Activity, language: Language = None, microphone: bool = True) -> Activity:
        for a in self.get_activities(microphone, language):
            if a.exercise_type != activity.exercise_type and a.skill == activity.skill:
                return a
        return None

    def get_discovery(self, skill: str, language: Language) -> Activity:
        activities = self.get_activities(language)
        for a in activities:
            if a.skill == skill and a.exercise_type not in ActivitiesManager.DISCOVERY_TYPES:
                return a
        return None

    def get_lower_level_activity(self, activity: Activity, language: Language = None, microphone: bool = True) -> Activity:
        first_match = None
        for a in self.get_activities(microphone, language):
            if a.level < activity.level:
                if first_match is None:
                    first_match = a
                if a.exercise_type != activity.exercise_type:
                    return a
        # If no exercise matched, we return the first match (without type condition)
        if first_match is not None:
            return first_match
        return None

    def get_activity(self, activity_id: str, language: Language = None) -> Activity:
        activities = self.get_activities(language)
        for a in activities:
            if a.id == activity_id:
                return a
        return None

    def get_activities(self, microphone: bool = True, language: Language = None) -> List[Activity]:
        activities = self.activities_by_language[language.name] if language is not None else self.activities
        if microphone:
            return activities
        return [a for a in activities if a.exercise_type != "reading"]

    def student_has_skill(self, student: Student, skill: str) -> bool:
        for t in student.traces:
            activity = self.get_activity(t.activity_id, student.language)
            if activity.skill == skill:
                return True
        return False
