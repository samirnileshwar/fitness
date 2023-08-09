import sys, getopt, random

push_core = ['Bench Press']
legs_core = ['Back Squat', 'Front Squat']
pull_core = ['Power Clean', 'Deadlift']

pull_a = ['Lat Pulldown', 'Cable Pulldown']
pull_b = ['Face Pull', 'Inverted Row', 'Deltoid Extension']
pull_c = ['Dumbell Snatch', 'Barbell Row', 'Classic Machine Row']
pull_d = ['Incline Bicep Curl', 'Preacher Curl', 'Shrugs']
pull_all = [pull_a, pull_b, pull_c, pull_d] 

push_a = ['Tricep Extension', 'Skull Crusher', 'Dips' ]
push_b = ['Shoulder Press', 'Dumbell Lateral Raise', 'Push Press']
push_c = ['Pushups', 'Chest Press', 'Incline Press', 'Chest Fly']
push_all = [push_a, push_b, push_c] 

legs_a = ['Single Leg DL', 'Back Extension', 'Dumbell RDL']
legs_b = ['Cable Hip Pull', 'Tibialis Raises']
legs_c = ['Leg Extension', 'Bulgarian Split Squat', 'Lunges']
legs_d = ['Hack Squat', 'Leg Press']
legs_all = [legs_a, legs_b, legs_c, legs_d] 

pull = []

def main(argv):
    core = argv[0]
    counts = {'push': 0, 'pull': 0, 'legs': 0}
    if core in push_core:
        counts['push'] += 1
    elif core in pull_core:
        counts['pull'] += 1
    elif core in legs_core:
        counts['legs'] += 1
    else:
        print("Core workout %s not known."%core)

    workouts = [core]

    while counts['push'] < 3:
        i = random.randrange(len(push_all))
        j = random.randrange(len(push_all[i]))
        workouts.append(push_all[i][j])
        del push_all[i]
        counts['push'] += 1

    while counts['pull'] < 3:
        i = random.randrange(len(pull_all))
        j = random.randrange(len(pull_all[i]))
        workouts.append(pull_all[i][j])
        del pull_all[i]
        counts['pull'] += 1

    while counts['legs'] < 3:
        i = random.randrange(len(legs_all))
        j = random.randrange(len(legs_all[i]))
        workouts.append(legs_all[i][j])
        del legs_all[i]
        counts['legs'] += 1

    print(workouts)


if __name__ == "__main__":
   main(sys.argv[1:])