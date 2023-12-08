#!/usr/bin/env python3

from WorkoutArchives import workouts

cyoa = workouts.CYOA() # Choose-Your-Own-Adventure Class
hit = workouts.HIT()   # High Intensity Training Class
pushups = workouts.Pushups() # Pushup Variations

# Select CYOA Workout
cyoa_yn = input("Select Choose-Your-Own-Adventure exercise? (y/n): ")
if cyoa_yn.lower() == 'y':
    cyoa.selectCYOA()

# Select HIT Workout
hit_yn = input("Select High Intensity exercise? (y/n): ")
if hit_yn.lower() == 'y':
    hit.selectHIT()

# Select Pushup Variations
pushup_yn = input("Select Pushup Variations? (y/n): ")
if pushup_yn.lower() == 'y':
    pushups.selectPUP()

# Print Results
print('\n' + 'Your selected workouts for the week are:')
print('    ' + 'CYOA    - ' + cyoa.cyoa_wo)
print('    ' + 'HIT     - ' + hit.hit_wo)
print('    ' + 'Pushups - ' + pushups.pup0 + ' and ' + pushups.pup1)
