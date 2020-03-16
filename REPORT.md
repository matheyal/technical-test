# Report

Time spent: about 2h30

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

## Conclusion

### It took time to get started...

It took me some time to get the project started with the proper models and deserialization of the json document because I am not using Python daily and I had to search the web to find how to do most of it.

### Then I encountered some issues

I did not encounter any major issue, but I can still mention the following:
- I'm still not sure how the activities relate to one another, the link between them is not clear and it was hard to get a good idea just by browsing the file
- Linked to the above, I was not sure of what "the next issue" meant. Was it dependant on the id, or on the order in the activities file. I went with the order in the file.
- Trying to avoid unnessary complexity took me some time and led to some refactoring along the

### Improvement ideas

- Using a proper database would be a great way to simplify this code. It would make it way easier to find activities matching a set of criteria
- Adding some proper tests using a unit testing framework. It was difficult in the time frame of the exercise, espacially given that the expectations changed between the exercises, but it's always a good idea to test this kind of logic.
- If not using a database, maybe building several hashmaps when loading the data could have simplified the code (by id, by skill, by level, ...).