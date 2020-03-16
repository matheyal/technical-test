# Report

## Level 1

The class `ActivitiesManager` is used as the central point for manipulating activities. It loads them from the json then exposes methods to find one or many and the main `get_most_relevant_activity` method.

I used dedicated model classes to make it easier to manipulate the different objects. Using dicts makes it hard for people to know what they are manipulating.

## Level 2

Just added some conditions to the existing methods while trying to avoid re-iterating over the activities.

## Level 3

Added filter on microphone attribute when getting the list of activities. This way, every other call depending on this is affected by the rule.

## Level 4

Understood it this way: « if the activity that is going to be suggested is a new skill we should suggest a discovery instead, then we suggest an activity in this skill »

I'm not sure my code respects the first part of the sentence because I ran out of time.