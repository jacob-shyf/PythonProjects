#!/usr/bin/env python3

from WorkoutArchives import workouts

cyoa = workouts.CYOA() # Choose-Your-Own-Adventure Class
hit = workouts.HIT()   # High Intensity Training Class

# Set Defaults
cyoa_selection = 'Fly away Stanley, be free!'
hit_selection = 'Nut up or shut up!'

# Select CYOA Workout
cyoa_yn = input("Select Choose-Your-Own-Adventure exercise? (y/n): ")
if cyoa_yn.lower() == 'y':
    cyoa_selection = cyoa.selectCYOA()

# Select HIT Workout
hit_yn = input("Select High Intensity exercise? (y/n): ")
if hit_yn.lower() == 'y':
    hit_selection = hit.selectHIT()


# Print Results
print('\n' + 'Your selected workouts for the week are:')
print('    ' + 'CYOA - ' + cyoa_selection)
print('    ' + 'HIT  - ' + hit_selection)
