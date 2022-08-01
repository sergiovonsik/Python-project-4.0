# def to print the graphic apart

def result(x):
    x = x.replace("_", " ")
    print('---------')
    print(f'| {x[0]} {x[1]} {x[2]} |')
    print(f'| {x[3]} {x[4]} {x[5]} |')
    print(f'| {x[6]} {x[7]} {x[8]} |')
    print('---------')


# def to find where to draw "X"

def find_index():
    global index
    global x_axis
    global y_axis
    index = 'none'
    try:
        x_axis, y_axis = input().split(" ")
        x_axis = int(x_axis)
        y_axis = int(y_axis)
    except ValueError:
        print('You should enter numbers!')
        find_index()
    if type(x_axis) == int and type(y_axis) == int:
        pass
    else:
        print('You should enter numbers!')
        find_index()

    if x_axis == 1:
        if y_axis == 1:
            index = 0
        elif y_axis == 2:
            index = 1
        elif y_axis == 3:
            index = 2

    elif x_axis == 2:
        if y_axis == 1:
            index = 3
        elif y_axis == 2:
            index = 4
        elif y_axis == 3:
            index = 5

    elif x_axis == 3:
        if y_axis == 1:
            index = 6
        elif y_axis == 2:
            index = 7
        elif y_axis == 3:
            index = 8
    while index == 'none':
        print('Coordinates should be from 1 to 3!')
        find_index()
    while game[index] in ("X", "O"):
        print('This cell is occupied! Choose another one!')
        index = find_index()
    else:
        pass

    return int(index)


# ---def to print the result when de game ends-------
def result_coment(game):
    global game_status
    winpatterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2)]

    # -------------
    if any(all(game[i] == "X" for i in patrn) for patrn in winpatterns):
        print("X wins")
        game_status = "over"
    elif any(all(game[i] == "O" for i in patrn) for patrn in winpatterns):
        print("O wins")
        game_status = "over"
    elif "_" not in game:
        print("Draw")
        game_status = "over"
    else:
        pass


# --- def to replace "_" with X or O

def replace_X_O(x):
    global game
    global x_or_o
    resultado = ""
    games = list(game)
    games[index] = x_or_o
    for i in games:
        resultado += i
    return resultado



# ----VARIABLE STORAGE--------
x_or_o = "X"
x_axis = 0
y_axis = 0
game = '_________'
game_status = "in process"

# -----GAME CORE--------

result(game)
while game_status == "in process":
    index = find_index()
    game = replace_X_O(index)
    result(game)
    result_coment(game)
    if x_or_o == "X":
        x_or_o = "O"
    elif x_or_o == "O":
        x_or_o = "X"


# ----------------------
def result_coment():
    global game_status
    winpatterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2)]

    # -------------
    if any(all(game[i] == "X" for i in patrn) for patrn in winpatterns):
        print("X wins")
        game_status = "over"
    elif any(all(game[i] == "O" for i in patrn) for patrn in winpatterns):
        print("O wins")
        game_status = "over"
    elif "_" not in game:
        print("Draw")
        game_status = "over"
    else:
        pass
# --------------------------
