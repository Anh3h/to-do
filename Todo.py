import time as Time
from enum import Enum
import re


class Status(Enum):
    TODO = 1
    DONE = 2
    DOING = 3


class Todo:
    count = 0

    def __init__(self, task, time):
        self.setTask(task)
        self.setTime(time)
        self.setStatus(Status.TODO)
        self._id = (Todo.count + 1)

        Todo.count += 1

    def __str__(self):
        return str(self._id) + " | " + self._task + " | " + str(self._time.tm_hour) + ":" + str(self._time.tm_min) + " | " + self._status.name

    def setTask(self, task):
        if len(task) > 2:
            self._task = task
        else:
            raise ValueError("Invalid task: The task must be more than one character")

    def getTask(self):
        return self._task

    def setTime(self, time):
        if re.match(r'\d\d:\d\d', time):
            self._time = Time.strptime(time, '%H:%M')
        pass

    def getTime(self):
        return self._time

    def setStatus(self, status):
        self._status = status

    def getId(self):
        return self._id
