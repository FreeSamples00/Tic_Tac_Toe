import turtle as t
import time


def enter_button():  # calls from space bar, locks in placement and switches turns
    global p1_score, p2_score, players_turn, selected
    if selected == '':
        return
    if players_turn == 1:
        players_turn = 2
        cells[selected][3] = False
        player_highlight(2)
    elif players_turn == 2:
        players_turn = 1
        cells[selected][3] = False
        player_highlight(1)
    selected = ''
    for line in lines_of_three:
        if cells[line[0]][2] == cells[line[1]][2] == cells[line[2]][2] == 'x':
            p1_score += 1
            update_score()
            draw_line(line[3], line[4])
            time.sleep(1)
            line_turtle.clear()
            clear_grid()
            break
        if cells[line[0]][2] == cells[line[1]][2] == cells[line[2]][2] == 'circle':
            p2_score += 1
            update_score()
            draw_line(line[3], line[4])
            time.sleep(1)
            clear_grid()
            line_turtle.clear()
            players_turn, selected = 1, ''
            break
    open_space = False
    for cell in cells:
        if cell[2] == 'clear':
            open_space = True
            break
    if not open_space:
        cats_game()
        time.sleep(1)
        clear_grid()
        line_turtle.clear()


def cats_game():  # makes a big c
    window.tracer(False)
    line_turtle.goto(500, 900)
    line_turtle.write('C', font=('arial', 300, 'normal'), align='center')
    window.tracer(True)


def clear_grid():  # clears all placed marks
    for i in range(9):
        edit_cell(i, 'clear')
        cells[i][3] = True


def edit_cell(cell, shape):  # changes the cells marking, called by clicked
    turtle = pens[cell]
    t.tracer(False)
    turtle.clear()
    if shape == 'x':
        turtle.penup()
        turtle.goto(cells[cell][0] - 40, cells[cell][1] + 50)
        turtle.pendown()
        turtle.goto(cells[cell][0] + 40, cells[cell][1] - 50)
        turtle.penup()
        turtle.goto(cells[cell][0] - 40, cells[cell][1] - 50)
        turtle.pendown()
        turtle.goto(cells[cell][0] + 40, cells[cell][1] + 50)
        turtle.penup()
        turtle.goto(cells[cell][0], cells[cell][1])
    elif shape == 'circle':
        turtle.goto(cells[cell][0], cells[cell][1] - 50)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()
        turtle.goto(cells[cell][0], cells[cell][1])
    cells[cell][2] = shape
    t.tracer(True)


def clicked(x, y):  # calls from an onclick, determines cell clicked and takes appropriate action
    global selected
    if players_turn == 1:
        shape = 'x'
    if players_turn == 2:
        shape = 'circle'
    for i, c in enumerate(cells):
        if ((c[0] - 100) < x < (c[0] + 100)) and ((c[1] - 100) < y < (c[1] + 100)):
            if c[2] == 'clear' and (i == selected or selected == '') and c[3]:
                edit_cell(i, shape)
                selected = i
            elif (c[2] == 'x' or 'circle') and (i == selected or selected == '') and c[3]:
                edit_cell(i, 'clear')
                selected = ''
            break


def draw_line(xy, XY):  # draws a line, used for the grid
    window.tracer(False)
    line_turtle.goto(xy[0], xy[1])
    line_turtle.pendown()
    line_turtle.goto(XY[0], XY[1])
    line_turtle.penup()
    window.tracer(True)


def player_highlight(player):  # highlights which players turn it is
    global players_turn
    t.tracer(False)
    highlighter.clear()
    highlighter.setheading(0)
    if players_turn == 1:
        highlighter.goto(190, 102)
    if players_turn == 2:
        highlighter.goto(590, 102)
    highlighter.pendown()
    highlighter.fd(230)
    highlighter.right(90)
    highlighter.fd(55)
    highlighter.right(90)
    highlighter.fd(230)
    highlighter.right(90)
    highlighter.fd(55)
    highlighter.penup()
    t.tracer(True)


def update_score():  # updates the score onscreen
    global p1_score, p2_score
    t.tracer(False)
    t_score1.clear()
    t_score2.clear()
    t_score1.write(f'Player 1: {p1_score:.0f}', font=('times new roman', 20, 'bold'))
    t_score2.write(f'Player 2: {p2_score:.0f}', font=('times new roman', 20, 'bold'))
    t.tracer(True)


window = t.Screen()
window.title('Tic Tac Toe')

window.tracer(False)

pen_size = 10
players_turn = 1
p1_score = 0
p2_score = 0
t.setworldcoordinates(0, 1000, 1000, 0)

highlighter = t.Turtle()
highlighter.penup()
highlighter.color('red')
highlighter.hideturtle()
highlighter.pensize(pen_size)


grid_turtle = t.Turtle()
grid_turtle.speed(0)
grid_turtle.hideturtle()
grid_turtle.pensize(pen_size)
for coords in [[400, 200, 'down'], [600, 200, 'down'], [200, 400, 'right'], [200, 600, 'right']]:
    grid_turtle.penup()
    grid_turtle.goto(coords[0], coords[1])
    grid_turtle.pendown()
    if coords[2] == 'down':
        degrees = 90
    elif coords[2] == 'right':
        degrees = 0
    grid_turtle.setheading(degrees)
    grid_turtle.fd(600)
grid_turtle.penup()
grid_turtle.goto(500, 900)
grid_turtle.write('Press space to submit', font=('times new roman', 20, 'bold'), align='center')

line_turtle = t.Turtle()
line_turtle.hideturtle()
line_turtle.penup()
line_turtle.color('red')
line_turtle.pensize(pen_size)

t_score1 = t.Turtle()
t_score2 = t.Turtle()
for x, y, turtle in [[200, 100, t_score1], [600, 100, t_score2]]:
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x, y)

selected = ''
# line = [cell1, cell2, cell3, start_coord, end_coord]
lines_of_three = ([0, 1, 2, [300, 300], [700, 300]], [3, 4, 5, [300, 500], [700, 500]],
                  [6, 7, 8, [300, 700], [700, 700]], [0, 3, 6, [300, 300], [300, 700]],
                  [1, 4, 7, [500, 300], [500, 700]], [2, 5, 8, [700, 300], [700, 700]],
                  [0, 4, 8, [300, 300], [700, 700]], [6, 4, 2, [300, 700], [700, 300]])

# cell = [x_cord, y_cord, state, malleable]
cells = [[300, 300, 'clear', True], [500, 300, 'clear', True], [700, 300, 'clear', True],
         [300, 500, 'clear', True], [500, 500, 'clear', True], [700, 500, 'clear', True],
         [300, 700, 'clear', True], [500, 700, 'clear', True], [700, 700, 'clear', True]]
pens = []
for i in range(9):
    pens.append(t.Turtle())
    pens[i].penup()
    pens[i].hideturtle()
    pens[i].speed(0)
    pens[i].pensize(pen_size - 2)
    pens[i].goto(cells[i][0], cells[i][1])
update_score()
player_highlight(1)

window.onclick(clicked)
window.onkeypress(enter_button, 'space')
window.listen()
window.mainloop()
