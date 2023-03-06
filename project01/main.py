"""
Name: Mohammed S. Abu-daf @Shark
ID: 000000000
Topic:
    Artificial Intelligence: Vacuum Cleaner Agent.
    Agent Model: Simple Reflex Agent.

Contact:
    email: mohammed_abudaf@student.iugaza.edu.ps

"""

import time
from time import sleep
import random


class VacuumAgent:
    """
    Vacuum Cleaner: is A simple Reflex Agent that depends on the current state
                    of the environment
    Class Methods: Constructor -- init the vacuum cleaner & give it the initial world state
                   Get_Precept_Measure -- sensing the current state of the environment
                   Run_Vacuum_Cleaner -- update the precept sequence and take an action
                  Agent_World_View -- the agent telling you his thought and actions

    Example:
        agent = VacuumAgent(str(location), str(environment_state))
        # parameters should be strings
        # environment state should be "Clean" & "Dirty"
        # location should be "A" & "B"
    """

    def __init__(self, location: str, environment_state: str):
        self.current_location: str = location
        self.current_state: str = environment_state
        self.action: str = ''
        self.points: int = 0
        self.available_actions: list = ['suck', 'UP', 'DOWN']

    def get_precept_measure(self, world_location: str, world_state: str):
        """
        this function sense the world state as location and state (dirty || clean) and update the
        preset sequence of the agent according the environment stat
        :param world_location: str()
        :param world_state:  str()
        :return: None

        Example:
            agent.get_precept_measure('A', 'Dirty')
        """
        self.current_location = world_location
        self.current_state = world_state
        sleep(2)

    def run_vacuum_cleaner(self):
        """
        this function take an action according the current state of the environment
        it should run after using function get_precept_measure
        if the current state is dirty, the agent should stay on the location and start
        cleaning until it finish or "sense the environment state becomes clean
        if the current state of the environment is clean he should take an action to move
        to next location A or B, depends on the current location
        :return: None

        Example:
            agent.run_vacuum_cleaner()
        """
        if self.current_state == 'Dirty':
            self.action = 'Suck'

        elif self.current_location == 'A':
            self.action = 'DOWN'
            self.current_location = 'B'

        elif self.current_location == 'B':
            self.action = 'UP'
            self.current_location = 'A'

    def agent_world_view(self):
        """
        this function print the present of the agent and the location
        :return: Void(None)

        Example:
            agent.agent_world_view()
        output:
            The Environment state is ' Dirty ' so, the action is ' Suck ' now the location is ' A '
        """
        print("The Environment state is \'", self.current_state,
              "\' so, the action is \'", self.action,
              "\' now the location is \'", self.current_location, "\'")

    def performance_measure(self):
        """
        this function for calculating  performance_measure accroding the user of the agent
        which works as:
            if it is the agent precepts match the human precepts the human gives a point
            as a good feedback, else the human gives it 0

        this function works every 15 seconds arrocding the program calculations
        :return: Void
        """
        print("\nVacuum Cleaner Thinks the Location ", self.current_location, " is clean\n")
        print("Do you think it is too? (Give the agent Feed Back)\n"
              "\t 0: for not clear\n"
              "\t 1: for clear")
        print("the location state is ", self.current_state)

        choice = int(input("\t> "))

        if choice == 1:
            self.points = self.points + 1
        elif choice == 0:
            self.points = self.points
        else:
            print("the command isn't recognized")
        pass


def changeWorldState() -> str:
    """
    this function change the world state between clean and dirty
    made the probability fifty-fifty, the range is ten so that we see a change
    in the environment, and does not stick at
    :return: str
        dirty or clean

    Example:
        world_state: str = changeWorldState()

    """

    temp_state: str = 'Dirty'
    random_value = random.randrange(0, 10)
    if random_value < 5:
        temp_state = "Dirty"
    if random_value >= 5:
        temp_state = "Clean"

    sleep(3)
    return temp_state


def main():
    print("-------- running vacuum cleaner simulator ---------")

    world_state: str = changeWorldState()  # init the world state
    reflex_agent: VacuumAgent = VacuumAgent('A', world_state)  # init a vacuum cleaner instate object and giving it a
    # location and world state
    start_time: time = time.time()  # this is the start time depends on the starting program

    live_count_down: int = 60  # total agent Cycle of 60 seconds

    while True:
        current_time: time = time.time()

        reflex_agent.get_precept_measure(reflex_agent.current_location, world_state)
        reflex_agent.run_vacuum_cleaner()
        reflex_agent.agent_world_view()
        world_state = changeWorldState()

        live_count_down = live_count_down - 5  # to calculate the total cycle

        if live_count_down % 15 == 0:
            # if the simulation get 15, 30, 45, or 60 performance measure will run
            reflex_agent.performance_measure()

        if live_count_down == 0:
            # if the simulation gets 60 seconds works, it will stop
            break

    print("-------- stop vacuum cleaner simulator ---------\n")
    print("the performance measure = ", reflex_agent.points)


if __name__ == '__main__':
    main()
