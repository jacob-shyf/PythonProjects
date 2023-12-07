#!/usr/bin/env python3

from WorkoutArchives import workouts

cyoa = workouts.CYOA() # Choose-Your-Own-Adventure Class
hit = workouts.HIT()   # High Intensity Training Class

# Select CYOA Workout
cyoa_yn = input("Select Choose-Your-Own-Adventure exercise? (y/n): ")
if cyoa_yn.lower() == 'y':
    cyoa.selectCYOA()

# Select HIT Workout
hit_yn = input("Select High Intensity exercise? (y/n): ")
if hit_yn.lower() == 'y':
    hit.selectHIT()

# Print Results
print('\n' + 'Your selected workouts for the week are:')
print('    ' + 'CYOA - ' + cyoa.cyoa_wo)
print('    ' + 'HIT  - ' + hit.hit_wo)
