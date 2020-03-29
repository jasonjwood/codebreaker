import random


def choose_code():
    code = []
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    while len(values) > 3:
        pick_index = random.randint(0, len(values) - 1)
        code.append(values[pick_index])
        values.remove(values[pick_index])

    print(code)

    return code


def get_guess():
    # Get guess
    guess = input("Guess --> ")
    guess_ok = True

    # Check that guess is ok
    if len(guess) != 5:
        print('Guess must be 5 letters long, and only be A, B, C, D, E, F, G, H. (NOT5)')
        guess_ok = False
    else:
        letters_seen = []
        for letter in guess:
            if letter not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                print('Guess must be 5 letters long, and only be A, B, C, D, E, F, G, H. (BADCHAR)')
                guess_ok = False
                break

            if letter in letters_seen:
                print('Guess must only show A, B, C, D, E, F, G, H once each (DUPLICATE)')
                guess_ok = False
                break

            letters_seen.append(letter)

    return {'guess_ok': guess_ok, 'guess': guess}


def space_string(s):
    spaced = ''
    for letter in s:
        spaced = spaced + letter + ' '

    return spaced


def colour_guess(guess):
    coloured_guess = str(guess).replace('A', u'\u001b[40;1m\u001b[37;1m A ')
    coloured_guess = coloured_guess.replace('B', u'\u001b[41;1m\u001b[30;1m B ')
    coloured_guess = coloured_guess.replace('C', u'\u001b[42;1m\u001b[30;1m C ')
    coloured_guess = coloured_guess.replace('D', u'\u001b[43;1m\u001b[30;1m D ')
    coloured_guess = coloured_guess.replace('E', u'\u001b[44;1m\u001b[30;1m E ')
    coloured_guess = coloured_guess.replace('F', u'\u001b[45;1m\u001b[30;1m F ')
    coloured_guess = coloured_guess.replace('G', u'\u001b[46;1m\u001b[30;1m G ')
    coloured_guess = coloured_guess.replace('H', u'\u001b[47;1m\u001b[30;1m H ')

    coloured_guess = coloured_guess + u'\u001b[0m'
    return coloured_guess


def print_game_board(game_board):
    clear = '\n' * 100
    print(clear)

    count = 1
    for row in game_board:
        guess_spaced = colour_guess(row['guess'])
        check_spaced = space_string(row['check'])
        print('#' + str(count) + ' Guess: ' + guess_spaced + '          ' + check_spaced + '\n')
        count = count + 1


def check_guess(code, guess):
    return 'ALEX'


def main():
    # Randomly pick the code
    code = choose_code()

    game_board = []

    # Loop over turns
    is_solved = False
    while not is_solved:
        # Ask for guess
        guess_input = get_guess()

        if guess_input['guess_ok'] is False:
            continue

        # Check guess and show answer
        check = check_guess(code, guess_input['guess'])

        game_board.append({'guess': guess_input['guess'], 'check': check})
        print_game_board(game_board)

        if check == 'WINNER':
            is_solved = True


main()
