import random

# General Workout Selector
class WorkoutSelector:
    def __init__(self):
        self.workouts = {
                'CYOA' : 'Fly away Stanley, be free!',
                'HIT' : 'Nut up or shut up!',
                'X-Train' : 'Get \'er done!',
                'Pullups' : 'Pussy baby bitch!',
                'Pushups' : 'Pussy baby bitch!' }
        self.workout_options = []
        self.last_workout = ''

    def getBlacklist(self, wo_type):
        blacklist = []

        if wo_type == 'CYOA':
            # High impact activities are off-limits for CYOA
            blacklist = ['Barefoot Jogging\n', 'Lacrosse\n']
        elif wo_type == 'X-Train':
            cyoa_wo = self.workouts['CYOA'] + '\n'
            ub_endurance = ['Swimming\n', 'Rowing\n', 'Climbing\n']
            if cyoa_wo in ub_endurance:
                # CYOA workout is an upper body endurnace workout,
                # blacklist upperbody endurance cross training
                for wo in ub_endurance:
                    blacklist.append(wo)
            else:
                # CYOA workout is not an upper-body endurance workout,
                # must select an upper-body endurance workout for
                # cross training
                for wo in self.workout_options:
                    if wo not in ub_endurance:
                        blacklist.append(wo)

        return blacklist
    
    def selectWorkout(self, wo_type):
        #check for valid name
        if wo_type not in self.workouts:
            return 'Invalid workout type!'
        
        # Define filenames
        options_file = 'WorkoutArchives/' + wo_type + '/' + wo_type.lower() + '.txt'
        last_wo_filename = 'WorkoutArchives/' + wo_type + '/prev_' + wo_type.lower() + '.txt'

        # Get exercise options
        options_file = open(options_file, 'r')
        self.workout_options = options_file.readlines()
        options_file.close()

        # Get last workout
        last_wo_file = open(last_wo_filename, 'r')
        self.last_workout = last_wo_file.readline()
        last_wo_file.close()

        # Get Off Limits exercises
        blacklist = self.getBlacklist(wo_type)

        #Generate a random workout selection
        self.workouts[wo_type] = random.choice(self.workout_options)
        while self.workouts[wo_type] == self.last_workout or blacklist.count(self.workouts[wo_type]):
            self.workouts[wo_type] = random.choice(self.workout_options)

        # Store workout selections
        last_wo_file = open(last_wo_filename, 'w')
        last_wo_file.write(self.workouts[wo_type])
        last_wo_file.close()

        self.workouts[wo_type] = self.workouts[wo_type].strip()
