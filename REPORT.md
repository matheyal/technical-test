# Report

## Level 1

The class `ActivitiesManager` is used as the central point for manipulating activities. It loads them from the json then exposes methods to find one or many and the main `get_most_relevant_activity` method.

I used dedicated model classes to make it easier to manipulate the different objects. Using dicts makes it hard for people to know what they are manipulating.

## Level 2

Just added some conditions to the existing methods while trying to avoid re-iterating over the activities.