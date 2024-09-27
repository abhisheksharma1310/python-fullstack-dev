# Object Oriented Programming
# Make a class Robot (Only define the class do not print anything or make an object in this solution pane (you can do that on your local machine))
# The Robot class will have the following attributes
# -> name , speed, job
# The Robot class will also have a function called clean_room, get_name, get_job
# the clean_room function
# ->the clean room function argument is time
# it  will take the time it takes to do the job and return the time it takes to do the job.
# It will calculate this time using the formula time / speed
# get_name function
# it simply returns the name of robot
# get_job function
# it will simply return the job of the robot
# you are only supposed to define this class.

class Robot:
    def __init__(self, name, speed, job):
        self.name = name
        self.speed = speed
        self.job = job

    def clean_room(self, time):
        return time/self.speed
    def get_name(self):
        return self.name
    def get_job(self):
        return self.job