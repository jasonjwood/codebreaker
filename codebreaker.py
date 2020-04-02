import random


def choose_code():
    code = []
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    while len(values) > 3:
        pick_index = random.randint(0, len(values) - 1)
        code.append(values[pick_index])
        values.remove(values[pick_index])

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
        print('#' + str(count) + ' Guess: ' + guess_spaced + '           Result: ' + row['check'] + '\n')
        count = count + 1


def check_guess(code, guess):
    num_stars = 0
    num_checkmarks = 0

    index = 0
    for letter in guess:
        # Is it the right letter in the right place?
        if letter == code[index]:
            num_stars = num_stars + 1
        # Is it the right letter but NOT in the right place?
        elif letter in code:
            num_checkmarks = num_checkmarks + 1

        index = index + 1

    # Print result of checking on the screen
    result = ''
    if num_stars == 5:
        result = 'WINNER'
    else:
        while num_stars > 0:
            result = result + '@ '
            num_stars = num_stars - 1
        while num_checkmarks > 0:
            result = result + '! '
            num_checkmarks = num_checkmarks - 1

    return result


def main():
    game_board = []

    # Randomly pick the code
    code = choose_code()

    # Loop over turns
    game_over = False
    while not game_over:
        # Ask for guess
        guess_input = get_guess()

        if guess_input['guess_ok'] is False:
            continue

        # Check guess
        check = check_guess(code, guess_input['guess'])

        # Show game board
        game_board.append({'guess': guess_input['guess'], 'check': check})
        print_game_board(game_board)

        if check == 'WINNER':
            game_over = True


main()
