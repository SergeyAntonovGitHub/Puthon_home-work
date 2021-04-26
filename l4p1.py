from sys import argv

def wage():
    try:
        working_out, rate, perk = map(float, (argv[1:]))

        print(f'wage = {working_out * rate + perk}')
    except ValueError:
        pass

wage()