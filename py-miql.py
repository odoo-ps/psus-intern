import curses 
from random import randint


WINDOW_WIDTH = 20
WINDOW_HEIGHT = 10 

curses.initscr()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

snake = [(4, 4), (4, 3), (4, 2)]
food = (6, 6)

win.addch(food[0], food[1], curses.ACS_PI)

score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(100 + len(snake))

    prev_key = key
    event = win.getch()

    if event != -1:
        if event == curses.KEY_DOWN:
            if prev_key == curses.KEY_UP:
                key = prev_key
            else:
                key = event
        elif event == curses.KEY_UP:
            if prev_key == curses.KEY_DOWN:
                key = prev_key
            else:
                key = event
        elif event == curses.KEY_RIGHT:
            if prev_key == curses.KEY_LEFT:
                key = prev_key
            else:
                key = event
        elif event == curses.KEY_LEFT:
            if prev_key == curses.KEY_RIGHT:
                key = prev_key
            else:
                key = event

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    if y == 0: break
    if y == WINDOW_HEIGHT-1: break
    if x == 0: break
    if x == WINDOW_WIDTH -1: break

    if snake[0] in snake[1:]: break

    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,WINDOW_HEIGHT-2), randint(1,WINDOW_WIDTH -2))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND)

curses.endwin()
print(f"Final score = {score}")