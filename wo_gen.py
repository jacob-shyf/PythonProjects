#!/usr/bin/env python3

from WorkoutArchives import workouts

ws = workouts.WorkoutSelector() # Workout Selector

#select CYOA Workout
cyoa_yn = input("Select Choose-Your-Own-Adventure exercise? (y/n): ")
if cyoa_yn.lower() == 'y':
    ws.selectWorkout('CYOA')

# Select Pushup Variation
pushup_yn = input("Select Pushup variation? (y/n): ")
if pushup_yn.lower() == 'y':
    ws.selectWorkout('Pushups')

# Selec Pullup Variation
pullup_yn = input("Select Pullup variation? (y/n): ")
if pullup_yn.lower() == 'y':
    ws.selectWorkout('Pullups')

# Select Cross Training Modality
xTrain_yn = input("Select Cross training modality? (y/n): ")
if xTrain_yn.lower() == 'y':
    ws.selectWorkout('X-Train')


# Print Results
print('\n' + 'Your selected workouts for the week are:')
print('    ' + 'CYOA    - ' + ws.workouts['CYOA'])
print('    ' + 'Pushups - ' + ws.workouts['Pushups'])
print('    ' + 'Pullups - ' + ws.workouts['Pullups'])
print('    ' + 'Cross Training - ' + ws.workouts['X-Train'])
