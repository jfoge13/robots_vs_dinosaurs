from robots import Robots

class Fleet:

    def __init__(self):
        self.fleet = []

    def add_robots(self):
        robot1 = Robots.name("Terminator")
        robot2 = Robots.name("R2D2")
        robot3 = Robots.name("Iron Giant")

        self.fleet.append(robot1)
        self.fleet.append(robot2)
        self.fleet.append(robot3)
        

