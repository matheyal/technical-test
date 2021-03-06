import enum


class Language(enum.Enum):
    FR = 1
    EN = 2


class Activity:

    def __init__(self, id: int, language: Language, exercise_type: str, skill: str, level: int):
        self.id: int = id
        self.language: Language = language
        self.exercise_type: str = exercise_type
        self.skill: str = skill
        self.level: int = level

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class Student:

    def __init__(self, language: Language, microphone: bool = False):
        self.language: Language = language
        self.traces: List[StudentTrace] = []
        self.microphone = microphone


class StudentTrace:
    """
    A list of traces corresponding to the activities the student previously finished. 
    Traces are chronologically ordered (latest to oldest).
    """

    def __init__(self, activity_id: int, score: float):
        self.activity_id: int = activity_id
        self.score: float = score
