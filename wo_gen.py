#!/usr/bin/env python2

class AllAround_2024:
    def __init__(self):
        self.hit = 'aa24_hit.txt'
        self.cyoa = 'aa24_cyoa.txt'
        self.prev_file = 'last_wo.txt'
        self.blacklist = ['Lacrosse Workout']
        
    def __deinit__(self):
        # Close files
        return 1

    def selectCYOA(self):
        return 'CYOA Workout'

    def selectHIT(self):
        return 'High Intensity Workout'

    def workoutGenerator(self):
        # Select CYOA Workout (if user requests one)
        cyoa_selection = raw_input("Select Choose-Your-Own-Adventure exercise? (y/n): ")
        if cyoa_selection.lower() == 'y':
            cyoa_selection = self.selectCYOA()
        
        # Select HIT Workout (if user requests one)
        hit_selection = raw_input("Select High Intensity exercise? (y/n): ")
        if hit_selection.lower() == 'y':
            hit_selection = self.selectHIT()

        # Print Selected workouts
        print('\n' + 'Your selected workouts for the week are:')
        if cyoa_selection.lower() != 'n':
            print('    ' + 'CYOA - ' + cyoa_selection)
        else:
            print('    ' + 'CYOA - Fly away Stanley, be free!')

        if hit_selection.lower() != 'n':
            print('    ' + 'HIT  - ' + hit_selection)
        else:
            print('    ' + 'HIT  - Nut up or shut up!')

if __name__ == '__main__':
    wo_gen = AllAround_2024()
    wo_gen.workoutGenerator()
