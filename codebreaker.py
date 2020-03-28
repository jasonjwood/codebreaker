import random


def choose_code():
    code = []
    values = ['A', 'B', 'C', 'D', 'E']

    while len(values) > 0:
        pick_index = random.randint(0, len(values) - 1)
        code.append(values[pick_index])
        values.remove(values[pick_index])

    print(code)



def main():
    #Randomly pick the code
    choose_code()
    #Loop over turns




main()