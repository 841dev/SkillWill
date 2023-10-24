class Heart:
    def __init__(self, usage: int):
        self.usage = usage
    @property
    def state(self):
        if self.usage > 70:
            return "high blood pressure"
        else:
            return "feeling good"

class Brain:
    def __init__(self, usage: int):
        self.usage = usage

    @property
    def state(self):
        if self.usage >90:
            return "tired"
        else:
            return "rested"

class Leg:
    def __init__(self, moving_speed):
        self.moving_speed = moving_speed

    @property
    def speed(self):
        if self.moving_speed < 11 and self.moving_speed > 0:
            return "walking"
        elif self.moving_speed > 10:
            return "runing"
        elif self.moving_speed == 0:
            return "standing"
        else:
            raise ValueError ("speed cannot be less than 0")

class Person:
    def __init__(self, heart, brain):
        self.heart = heart
        self.brain = brain



heart = Heart(65)
brain = Brain(85)
leg = Leg(7)

person = Person(heart, brain)
person.leg = leg

print(f"Persons heart usage is {person.heart.usage}-bpm and thats why state is: {person.heart.state}")
print(f"Persons brain usage is {person.brain.usage}-% and thats why he feels '{person.brain.state}'")

print(f"Person is {person.leg.speed}")

