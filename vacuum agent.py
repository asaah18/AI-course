# simple AI agent(vacuum cleaner), using if statement style
# where the agent move between rooms -also called location- A,B

import sys
from random import randint


class VacuumCleaner:
    possible_locations = ("A", "B")
    possible_states = ("C", "D")

    def __init__(self):
        # get initial location from user
        user_input = input("Enter the location of the Agent(A[room] or B[room]): ")
        self.location = user_input[0].upper()

        # check user input
        if self.location not in self.possible_locations:
            print("The location is wrong, run the program again")
            sys.exit()

        print("The Agent starts at:", self.location)
        # get number of agent's actions
        times = int(input("Enter the number of the Agent's actions:"))
        # do actions
        print("-" * 55)
        for counter in range(times):
            self.reflex_vacuum_agent()
            print()

    def reflex_vacuum_agent(self):
        # get state of room from sensor
        state = None
        state = self.sensor()

        if state is not None:
            next_location = self.get_next_location()
            # dirty room
            if state == "D":
                print(self.location + " [Detected-Dirty], Action: clean and go to the location " + next_location)
            # clean room
            else:
                print(self.location + " [Detected-clean], Action: go to Location " + next_location)
            self.location = next_location
        # no response from sensor
        else:
            print("Unexpected failure with detecting the location state,try again")

    def sensor(self):
        return self.possible_states[randint(0, (len(self.possible_states) - 1))]

    def get_next_location(self):
        if self.location == "A":
            return "B"
        else:
            return "A"


VacuumCleaner()
