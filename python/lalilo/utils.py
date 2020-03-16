import json
from collections import defaultdict
from typing import List, Dict
from lalilo.model import *


class ActivitiesManager():
    """
    Loads activities and offers method to manipulate them
    """

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

        # If perfect score on last activity
        last_activity: Activity = self.get_activity(
            student.traces[0].activity_id, student.language)
        if student.traces[0].score == 1.0:
            return self.get_next_activity(last_activity, student.language)
        lower_level = self.get_lower_level_activity(
            last_activity, student.language)
        if lower_level is not None:
            return lower_level
        return last_activity

    def get_next_activity(self, activity: Activity, language: Language = None) -> Activity:
        activities = self.activities_by_language[language.name]
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

    def get_lower_level_activity(self, activity: Activity, language: Language = None) -> Activity:
        first_match = None
        for a in self.get_activities(language):
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

    def get_activities(self, language: Language = None) -> List[Activity]:
        if language is not None:
            return self.activities_by_language[language.name]
        else:
            return self.activities
