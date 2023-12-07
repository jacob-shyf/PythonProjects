import random

# High Intensity Training
class HIT:
    def __init__(self):
        self.hit = 'hit.txt'
        self.prev_hit = 'prev_hit.txt'
        self.archive = 'WorkoutArchives/HIT/'
        self.hit_wo = 'Nut up or shut up!'
        self.blacklist = []

    def selectHIT(self):
        # Read CYOA workout options
        hit_file = open(self.archive + self.hit, 'r')
        hit_options = hit_file.readlines()
        hit_file.close()

        # Read previous workout selection
        prev_hit_file = open(self.archive + self.prev_hit, 'r')
        prev_wo = prev_hit_file.readline()
        prev_hit_file.close()
        
        # Generate a random choice that isn't blacklisted or the previous choice
        self.hit_wo = random.choice(hit_options)
        while self.hit_wo == prev_wo or self.blacklist.count(self.hit_wo):
            self.hit_wo = random.choice(hit_options)

        # Save workout selection
        prev_hit_file = open(self.archive + self.prev_hit, 'w')
        prev_hit_file.write(self.hit_wo)
        prev_hit_file.close()

        self.hit_wo = self.hit_wo.strip()

# Choose-Your-Own-Adventure (Activitiy Ideas)
class CYOA:
    def __init__(self):
        self.cyoa = 'cyoa.txt'
        self.prev_cyoa = 'prev_cyoa.txt'
        self.archive = 'WorkoutArchives/CYOA/'
        self.cyoa_wo = 'Fly away Stanley, be free!'
        self.blacklist = ['Lacrosse Workout\n']

    def selectCYOA(self):
        # Read CYOA workout options
        cyoa_file = open(self.archive + self.cyoa, 'r')
        cyoa_options = cyoa_file.readlines()
        cyoa_file.close()

        # Read previous workout selection
        prev_cyoa_file = open(self.archive + self.prev_cyoa, 'r')
        prev_wo = prev_cyoa_file.readline()
        prev_cyoa_file.close()

        # Generate a random choice that isn't blacklisted or the previous choice
        self.cyoa_wo = random.choice(cyoa_options)
        while self.cyoa_wo == prev_wo or self.blacklist.count(self.cyoa_wo):
            self.cyoa_wo = random.choice(cyoa_options)

        # Save workout selection
        prev_cyoa_file = open(self.archive + self.prev_cyoa, 'w')
        prev_cyoa_file.write(self.cyoa_wo)
        prev_cyoa_file.close()

        self.cyoa_wo = self.cyoa_wo.strip()
