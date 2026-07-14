class Adventure:
    """adventure class will store the title of the adventure, number of people, and each day"""
    def __init__(self, title):
        self.title = title
        self.people = []
        self.days = []

class Day:
    """Day class will store the day of the adventure and activities to be done."""
    def __init__(self, day):
        self.day = day
        self.activities = []

class Activity:
    """Activity class will store the activity, type of activity, and day it will be done"""
    def __init__(self, activity, kind, day):
        self.activity = activity
        self.kind = kind
        self.day = day