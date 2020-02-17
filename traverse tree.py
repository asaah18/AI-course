from collections import deque


class TraverseTree:
    # initiate adjacency list   |   graph
    adjLists_dict = {}
    current_city = None

    def __init__(self):
        self.setup_graph()
        self.starting_city()
        self.traverse()

    def setup_graph(self):
        self.adjLists_dict["Buraydah"] = ["Unayzah", "Riyadh-Alkhabra", "Al-Bukayriyah"]
        self.adjLists_dict["Unayzah"] = ["AlZulfi", "Al-Badai", "Buraydah"]
        self.adjLists_dict["Riyadh-Alkhabra"] = ["Buraydah", "Al-Badai"]
        self.adjLists_dict["Al-Bukayriyah"] = ["Buraydah", "Sheehyah"]
        self.adjLists_dict["AlZulfi"] = ["Unayzah", "UmSedrah"]
        self.adjLists_dict["Al-Badai"] = ["Unayzah", "Riyadh-Alkhabra", "AlRass"]
        self.adjLists_dict["Sheehyah"] = ["Al-Bukayriyah", "Dhalfa"]
        self.adjLists_dict["UmSedrah"] = ["AlZulfi", "Shakra"]
        self.adjLists_dict["AlRass"] = ["Al-Badai"]
        self.adjLists_dict["Dhalfa"] = ["Sheehyah", "Mulaida"]
        self.adjLists_dict["Shakra"] = ["UmSedrah"]
        self.adjLists_dict["Mulaida"] = ["Dhalfa"]

    def get_cities(self):
        return [city for city in self.adjLists_dict.keys()]

    @staticmethod
    def get_user_choice(choices):
        """
        get choice of user from the given choices as an integer, starting from 0
        :param choices: list
        :return user_input: int
        """
        # print choices
        for index, choice in enumerate(choices):
            print("[" + str(index) + "] " + choice)
        # get user input
        while True:
            user_input = input("\n" + "input: ")
            if (user_input.isdigit() is False) or (int(user_input) not in range(len(choices))):
                print("wrong input!")
            else:
                return int(user_input)

    def starting_city(self):
        cities = self.get_cities()
        print("Choose a city number to start with:" + "\n")
        self.current_city = cities[self.get_user_choice(cities)]

    def traverse(self):
        traverse_choices = ["manually", "First In First Out(FIFO)", "Last In First Out (LIFO)", "Stop"]
        print("----------Traverse-------------")
        while True:
            print("The current location is:", self.current_city)
            print()
            print("Moving to the next destination:")
            user_choice = self.get_user_choice(traverse_choices)

            if user_choice == 0:
                # manual traverse
                self.manual_traverse()
            elif user_choice == 1:
                # First In First Out(FIFO) | queue
                self.queue_traverse()
            elif user_choice == 2:
                # Last In First Out (LIFO) | stack
                self.stack_traverse()
            elif user_choice == 3:
                # stop
                print("thank you for using our airline services :)")
                break

    def manual_traverse(self):
        print("Choose one of the following connected cities:")
        connected_cities = self.get_connected_cities()
        user_choice = self.get_user_choice(connected_cities)
        self.current_city = connected_cities[user_choice]

    def queue_traverse(self):
        # add connected cities to queue
        queue = deque(self.get_connected_cities())
        # represent the queue
        print(list(queue))
        # dequeue
        destination = queue.popleft()
        # traverse to the city you get
        self.current_city = destination
        print(self.current_city, "is the destination\n")
        pass

    def stack_traverse(self):
        # add connected cities to stack
        stack = self.get_connected_cities()
        # represent the stack
        print(stack)
        # pop up
        destination = stack.pop()
        # traverse to the city you get
        self.current_city = destination
        print(self.current_city, "is the destination\n")

    def get_connected_cities(self):
        return self.adjLists_dict[self.current_city]


TraverseTree()
