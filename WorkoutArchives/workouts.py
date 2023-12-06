import random

# High Intensity Training
class HIT:
    def __init__(self):
        self.hit = 'hit.txt'
        self.prev_hit = 'prev_hit.txt'
        self.archive = 'WorkoutArchives/HIT/'
        self.blacklist = []

    def selectHIT(self):
        return 'HIT Workout'

# Choose-Your-Own-Adventure (Activitiy Ideas)
class CYOA:
    def __init__(self):
        self.cyoa = 'cyoa.txt'
        self.prev_cyoa = 'prev_cyoa.txt'
        self.archive = 'WorkoutArchives/CYOA/'
        self.blacklist = ['Lacrosse Workout\n']

    def selectCYOA(self):
        # Read CYOA workout options
        cyoa_file = open(self.archive + self.cyoa, 'r')
        cyoa_options = cyoa_file.readlines()
        cyoa_file.close()

        # Read previous workout selection
        prev_cyoa_file = open(self.archive + self.prev_cyoa, 'r')
        prev_wo = prev_cyoa_file.readlines()
        prev_cyoa_file.close()

        # Generate a random choice that isn't blacklisted or the previous choice
        cyoa_wo = random.choice(cyoa_options)
        while cyoa_wo == prev_wo or self.blacklist.count(cyoa_wo):
            cyoa_wo = random.choice(cyoa_options)

        # Save workout selection
        prev_cyoa_file = open(self.archive + self.prev_cyoa, 'w')
        prev_cyoa_file.write(cyoa_wo)
        prev_cyoa_file.close()

        return cyoa_wo.strip()
